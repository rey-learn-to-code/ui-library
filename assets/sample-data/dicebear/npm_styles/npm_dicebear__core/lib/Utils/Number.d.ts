/**
 * Formats a number for SVG output, rounded to at most 5 decimal places.
 *
 * Rounding to a fixed precision keeps the output bounded and identical across
 * every port: every value becomes a multiple of 1e-5 in the SVG coordinate
 * range, which has no exponential form, so the result is built from integer
 * arithmetic (no locale- or language-specific float stringifying). Five
 * decimals is far below sub-pixel precision for any realistic canvas.
 */
export declare class Number {
    static format(value: number): string;
}
