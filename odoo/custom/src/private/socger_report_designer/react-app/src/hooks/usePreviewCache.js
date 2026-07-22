import {useRef, useCallback} from "react";

/**
 * Client-side preview cache with in-memory Map + sessionStorage fallback.
 *
 * Cache keys are SHA-256-like hashes of (layout_json + target_model + record_id).
 * Entries expire after ``TTL_MS`` milliseconds (default 5 minutes).
 *
 * Usage:
 *   const {get, set, invalidate} = usePreviewCache();
 *   const cached = get(cacheKey);
 *   if (cached) return cached;
 *   const html = await fetchPreview(...);
 *   set(cacheKey, html);
 */
const TTL_MS = 5 * 60 * 1000; // 5 minutes
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

/**
 * Try to load sessionStorage on mount.
 */
function loadFromSession(key) {
    try {
        const raw = sessionStorage.getItem(key);
        if (!raw) return null;
        const entry = JSON.parse(raw);
        if (Date.now() - entry.ts > TTL_MS) {
            sessionStorage.removeItem(key);
            return null;
        }
        return entry.value;
    } catch {
        return null;
    }
}

function saveToSession(key, value) {
    try {
        sessionStorage.setItem(key, JSON.stringify({value, ts: Date.now()}));
    } catch {
        // Storage full — silently ignore
    }
}

export default function usePreviewCache() {
    const memCache = useRef(new Map());

    const get = useCallback((layoutJson, targetModel, recordId) => {
        const key = hashKey([layoutJson, targetModel, String(recordId || "")]);
        const sessionKey = `preview_cache_${key}`;

        // 1. Check in-memory
        const memEntry = memCache.current.get(key);
        if (memEntry && Date.now() - memEntry.ts < TTL_MS) {
            return memEntry.value;
        }
        memCache.current.delete(key);

        // 2. Check sessionStorage
        return loadFromSession(sessionKey);
    }, []);

    const set = useCallback((layoutJson, targetModel, recordId, value) => {
        const key = hashKey([layoutJson, targetModel, String(recordId || "")]);
        const sessionKey = `preview_cache_${key}`;

        memCache.current.set(key, {value, ts: Date.now()});

        // Evict oldest if over limit
        if (memCache.current.size > MAX_ENTRIES) {
            const oldest = memCache.current.keys().next().value;
            memCache.current.delete(oldest);
        }

        saveToSession(sessionKey, value);
    }, []);

    const invalidate = useCallback((layoutJson, targetModel, recordId) => {
        const key = hashKey([layoutJson, targetModel, String(recordId || "")]);
        memCache.current.delete(key);
        try {
            sessionStorage.removeItem(`preview_cache_${key}`);
        } catch {
            // ignore
        }
    }, []);

    const invalidateAll = useCallback(() => {
        memCache.current.clear();
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
    }, []);

    return {get, set, invalidate, invalidateAll};
}
