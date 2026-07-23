import {useRef, useCallback} from "react";

/**
 * Client-side preview cache — in-memory only (no sessionStorage).
 *
 * Using in-memory Map avoids stale data when the user saves a layout,
 * navigates away, and comes back.  Each component mount starts with a
 * fresh cache.  The TTL is short (2 minutes) so even within a session
 * the preview stays reasonably current.
 *
 * Cache keys are hashes of (layout_json + target_model + record_id +
 * paper_format + paper_orientation).
 *
 * Usage:
 *   const {get, set, invalidate, invalidateAll} = usePreviewCache();
 */
const TTL_MS = 2 * 60 * 1000; // 2 minutes
const MAX_ENTRIES = 50;

/**
 * Simple hash function for cache keys — not cryptographic, just fast.
 */
function hashKey(parts) {
    let hash = 0;
    const str = parts.join("||");
    for (let i = 0; i < str.length; i++) {
        const ch = str.charCodeAt(i);
        hash = (hash << 5) - hash + ch;
        hash |= 0; // Convert to 32-bit int
    }
    return `pc_${Math.abs(hash).toString(36)}`;
}

export default function usePreviewCache() {
    const memCache = useRef(new Map());

    const get = useCallback(
        (layoutJson, targetModel, recordId, paperFormat, paperOrientation) => {
            const key = hashKey([
                layoutJson,
                targetModel,
                String(recordId || ""),
                String(paperFormat || ""),
                String(paperOrientation || ""),
            ]);
            const entry = memCache.current.get(key);
            if (entry && Date.now() - entry.ts < TTL_MS) {
                return entry.value;
            }
            memCache.current.delete(key);
            return null;
        },
        []
    );

    const set = useCallback(
        (layoutJson, targetModel, recordId, value, paperFormat, paperOrientation) => {
            const key = hashKey([
                layoutJson,
                targetModel,
                String(recordId || ""),
                String(paperFormat || ""),
                String(paperOrientation || ""),
            ]);
            memCache.current.set(key, {value, ts: Date.now()});

            // Evict oldest if over limit
            if (memCache.current.size > MAX_ENTRIES) {
                const oldest = memCache.current.keys().next().value;
                memCache.current.delete(oldest);
            }
        },
        []
    );

    const invalidate = useCallback(
        (layoutJson, targetModel, recordId, paperFormat, paperOrientation) => {
            const key = hashKey([
                layoutJson,
                targetModel,
                String(recordId || ""),
                String(paperFormat || ""),
                String(paperOrientation || ""),
            ]);
            memCache.current.delete(key);
        },
        []
    );

    const invalidateAll = useCallback(() => {
        memCache.current.clear();
    }, []);

    // Also clear any legacy sessionStorage entries from previous versions
    try {
        const keys = Object.keys(sessionStorage);
        for (const k of keys) {
            if (k.startsWith("preview_cache_")) {
                sessionStorage.removeItem(k);
            }
        }
    } catch {
        // ignore
    }

    return {get, set, invalidate, invalidateAll};
}
