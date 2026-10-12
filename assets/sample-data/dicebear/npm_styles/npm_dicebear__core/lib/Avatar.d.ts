import { Style } from './Style.js';
import type { StyleOptions } from './StyleOptions.js';
type UnwrapStyle<D> = D extends Style<infer S> ? S : D;
interface AvatarJson<D = unknown> {
    readonly svg: string;
    readonly options: StyleOptions<UnwrapStyle<D>>;
}
/**
 * Top-level entry point for rendering an avatar from a style and options.
 *
 * Construction immediately resolves and renders the SVG; the various
 * accessor methods return different serializations of that result.
 */
export declare class Avatar<D = unknown> {
    #private;
    /**
     * Pass a {@link Style} instance. Passing a raw style definition is
     * deprecated and will be removed in v11; wrap it with `new Style(...)` and
     * reuse the instance across avatars.
     */
    constructor(styleInput: D, optionsInput?: StyleOptions<UnwrapStyle<D>>);
    /**
     * Returns the rendered SVG markup.
     */
    toString(): string;
    /**
     * Returns the avatar as a JSON-serializable object containing the SVG and
     * the fully resolved options used to render it.
     */
    toJSON(): AvatarJson<D>;
    /**
     * Returns the SVG encoded as a `data:image/svg+xml` URI.
     */
    toDataUri(): string;
}
export {};
