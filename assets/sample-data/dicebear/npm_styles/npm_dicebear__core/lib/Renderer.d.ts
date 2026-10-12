import type { Style } from './Style.js';
import type { Resolver } from './Resolver.js';
/**
 * Walks a style's element tree and turns it into the final SVG markup.
 *
 * The renderer is single-use: it accumulates `<defs>` entries and per-render
 * caches across method calls, so a fresh instance is required per avatar.
 */
export declare class Renderer {
    #private;
    constructor(style: Style, resolver: Resolver);
    /**
     * Builds the complete SVG document for the avatar.
     */
    render(): string;
}
