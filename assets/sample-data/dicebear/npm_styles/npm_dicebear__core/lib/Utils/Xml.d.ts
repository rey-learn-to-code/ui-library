/**
 * Minimal XML escaping helper for SVG/XML text and attribute content.
 */
export declare class Xml {
    #private;
    /**
     * Returns `value` with the five XML predefined entities escaped.
     */
    static escape(value: string): string;
}
