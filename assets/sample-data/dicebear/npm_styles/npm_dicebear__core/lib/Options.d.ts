import type { Range } from './StyleDefinition.js';
import type { StyleOptions, StyleOptionsFlipValue, StyleOptionsColorFillValue, StyleOptionsColorOrderValue, TagFilterToken } from './StyleOptions.js';
/**
 * Validates the raw user-supplied options and exposes them through typed
 * accessors. Each accessor returns the user's input in a normalized form
 * (always an array for options that accept either a scalar or an array, or
 * `undefined` when the option is not set), so consumers — chiefly
 * {@link Resolver} — never have to do their own normalization.
 *
 * Resolution against the style definition and the PRNG happens in
 * {@link Resolver}; this class is purely about reading user input.
 */
export declare class Options<D = unknown> {
    #private;
    constructor(data?: StyleOptions<D>);
    seed(): string | undefined;
    size(): number | undefined;
    idRandomization(): boolean | undefined;
    title(): string | undefined;
    flip(): readonly StyleOptionsFlipValue[];
    fontFamily(): readonly string[];
    fontWeight(): readonly number[];
    scale(): Range | undefined;
    borderRadius(): Range | undefined;
    rotate(): Range | undefined;
    translateX(): Range | undefined;
    translateY(): Range | undefined;
    /**
     * Returns the global `tags` filter as parsed tokens, or an empty array when
     * unset. Each raw token (`category` / `category:value`, optionally
     * `!`-prefixed to disallow) is decoded into `{ category, value?, negated }` so
     * the resolver composes the filter without parsing the grammar itself. An
     * empty list means no tag filtering (classic behavior). Memoized, since the
     * resolver reads it once per component.
     */
    tags(): readonly TagFilterToken[];
    /**
     * Returns the user-set variant constraint for `name` as a weighted map, or
     * `undefined` when `${name}Variant` is unset. A bare string or string list
     * is normalized to a map with each entry weighted `1`.
     */
    componentVariant(name: string): Readonly<Record<string, number>> | undefined;
    componentProbability(name: string): number | undefined;
    /**
     * Asymmetric on purpose: returns `undefined` (rather than `[]`) when
     * `${name}Color` is unset so the resolver can fall back to the style
     * definition's color values.
     */
    color(name: string): readonly string[] | undefined;
    colorFill(name: string): readonly StyleOptionsColorFillValue[];
    colorAngle(name: string): Range | undefined;
    colorFillStops(name: string): Range | undefined;
    colorOrder(name: string): StyleOptionsColorOrderValue | undefined;
}
