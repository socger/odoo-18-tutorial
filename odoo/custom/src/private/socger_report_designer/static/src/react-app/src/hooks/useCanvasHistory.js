import {useState, useCallback, useRef} from "react";

/**
 * Custom hook for undo/redo history on an array of elements.
 *
 * Maintains a stack of past states and a stack of future states.
 * Every call to `push` records the current state and replaces it with the new one.
 * `undo` reverts to the previous state; `redo` moves forward.
 *
 * @param {Array} initialElements - Starting elements array
 * @param {number} [maxHistory=50] - Max undo steps to keep
 */
export default function useCanvasHistory(initialElements = [], maxHistory = 50) {
    const [elements, setElements] = useState(initialElements);
    const pastRef = useRef([]);
    const futureRef = useRef([]);

    /** Push a new state (records current as undoable). */
    const push = useCallback(
        (newElements) => {
            setElements((prev) => {
                pastRef.current = [...pastRef.current.slice(-(maxHistory - 1)), prev];
                futureRef.current = [];
                return newElements;
            });
        },
        [maxHistory]
    );

    /** Undo — go back one step. */
    const undo = useCallback(() => {
        if (pastRef.current.length === 0) return;
        setElements((current) => {
            const prev = pastRef.current[pastRef.current.length - 1];
            pastRef.current = pastRef.current.slice(0, -1);
            futureRef.current = [...futureRef.current, current];
            return prev;
        });
    }, []);

    /** Redo — go forward one step. */
    const redo = useCallback(() => {
        if (futureRef.current.length === 0) return;
        setElements((current) => {
            const next = futureRef.current[futureRef.current.length - 1];
            futureRef.current = futureRef.current.slice(0, -1);
            pastRef.current = [...pastRef.current, current];
            return next;
        });
    }, []);

    const canUndo = pastRef.current.length > 0;
    const canRedo = futureRef.current.length > 0;

    return {elements, setElements, push, undo, redo, canUndo, canRedo};
}
