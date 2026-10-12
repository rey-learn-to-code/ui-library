/**
 * Color helpers used by the renderer and option resolver.
 */
export declare class Color {
    #private;
    /**
     * Normalizes any hex format to 6- or 8-digit lowercase with `#` prefix.
     */
    static toHex(hex: string): string;
    /**
     * Like {@link toHex}, but strips the alpha channel and always returns
     * 6-digit hex.
     */
    static toRgbHex(hex: string): string;
    /**
     * Parses a hex color into an `[r, g, b]` triple of 8-bit channel values.
     */
    static parseHex(hex: string): [number, number, number];
    /**
     * WCAG 2.1 relative luminance with sRGB linearization.
     *
     * @see https://www.w3.org/WAI/GL/wiki/Relative_luminance
     */
    static luminance(hex: string): number;
    /**
     * Returns a new array sorted by descending contrast against the reference
     * color.
     *
     * @see https://www.w3.org/WAI/GL/wiki/Contrast_ratio
     */
    static sortByContrast(candidates: readonly string[], refColor: string): string[];
    /**
     * Returns a new array with excluded colors removed. Falls back to the
     * original candidates when filtering would empty the list.
     */
    static filterNotEqualTo(candidates: readonly string[], excluded: readonly string[]): string[];
}
