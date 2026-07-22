import React, {useState, useCallback, useEffect, useRef} from "react";

/**
 * Lightweight toast notification system.
 *
 * Usage:
 *   const {showToast, ToastContainer} = useToast();
 *   showToast("Layout saved", "success");
 *   showToast("Error occurred", "error");
 *   showToast("Info message", "info");
 *
 * Returns a hook that provides showToast() and the ToastContainer component.
 */
let toastIdCounter = 0;

export function useToast() {
    const [toasts, setToasts] = useState([]);
    const timersRef = useRef(new Map());

    const removeToast = useCallback((id) => {
        if (timersRef.current.has(id)) {
            clearTimeout(timersRef.current.get(id));
            timersRef.current.delete(id);
        }
        setToasts((prev) => prev.filter((t) => t.id !== id));
    }, []);

    const showToast = useCallback(
        (message, variant = "info", durationMs = 4000) => {
            const id = ++toastIdCounter;
            setToasts((prev) => [...prev, {id, message, variant}]);
            if (durationMs > 0) {
                const timer = setTimeout(() => removeToast(id), durationMs);
                timersRef.current.set(id, timer);
            }
        },
        [removeToast]
    );

    // Cleanup all timers on unmount
    useEffect(() => {
        const timers = timersRef.current;
        return () => {
            for (const t of timers.values()) clearTimeout(t);
        };
    }, []);

    const ToastContainer = useCallback(
        () => (
            <div className="o_toast_container" aria-live="polite">
                {toasts.map((t) => (
                    <div
                        key={t.id}
                        className={`o_toast o_toast_${t.variant}`}
                        onClick={() => removeToast(t.id)}
                        title="Click to dismiss"
                    >
                        <i
                            className={`fa ${
                                t.variant === "success"
                                    ? "fa-check-circle"
                                    : t.variant === "error"
                                    ? "fa-times-circle"
                                    : t.variant === "warning"
                                    ? "fa-exclamation-circle"
                                    : "fa-info-circle"
                            } me-2`}
                        />
                        <span className="o_toast_message">{t.message}</span>
                        <button
                            className="o_toast_close"
                            onClick={(e) => {
                                e.stopPropagation();
                                removeToast(t.id);
                            }}
                        >
                            <i className="fa fa-times" />
                        </button>
                    </div>
                ))}
            </div>
        ),
        [toasts, removeToast]
    );

    return {showToast, ToastContainer};
}

export default useToast;
