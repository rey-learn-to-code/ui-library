/**
 * Thrown when a color in the style definition references itself, directly or
 * indirectly. The {@link chain} field reproduces the resolution path.
 */
export declare class CircularColorReferenceError extends Error {
    readonly chain: readonly string[];
    constructor(chain: readonly string[]);
}
