import type { Meta } from '../Style/Meta.js';
/**
 * Builds attribution strings and embedded RDF/Dublin Core metadata from a
 * style's {@link Meta} block.
 */
export declare class License {
    /**
     * Returns a single-line attribution string suitable for `<title>` or
     * `<desc>` content. Returns an empty string when no attribution data is
     * available.
     */
    static text(meta: Meta): string;
    /**
     * Builds an embedded `<metadata>` block with Dublin Core terms describing
     * the style's source, creator, license, and rights statement. Returns an
     * empty string when no metadata fields are populated.
     */
    static xml(meta: Meta): string;
}
