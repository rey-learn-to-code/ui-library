import { Options } from './Options.js';
import type { Style } from './Style.js';
import { type StyleOptionsFlipValue, type StyleOptionsColorFillValue, type StyleOptionsColorOrderValue, type StyleOptions } from './StyleOptions.js';
/**
 * Bundles the three inputs needed to derive any deterministic value for an
 * avatar — the {@link Style}, the validated user {@link Options}, and a
 * seeded {@link Prng} — and exposes them as named accessors. Each accessor
 * memoizes its result so that repeated calls cannot drift. The memo also
 * serves as the informational snapshot returned by {@link resolved} — every
 * value the resolver picks during one resolution lands there, except for
 * the raw seed.
 */
export declare class Resolver<D = unknown> {
    #private;
    constructor(style: Style<D>, options: Options<D>);
    seed(): string;
    size(): number | undefined;
    idRandomization(): boolean;
    title(): string | undefined;
    flip(): StyleOptionsFlipValue;
    fontFamily(): string;
    fontWeight(): number;
    scale(): number;
    borderRadius(): number;
    rotate(): number;
    translateX(): number;
    translateY(): number;
    /**
     * Selects a variant for the given component. The pool the PRNG draws from is
     * built from the per-component `${name}Variant` option and the global `tags`
     * filter (see {@link #variantWeights}). Only variants that exist in the style
     * definition are considered.
     */
    variant(name: string): string | undefined;
    color(name: string): readonly string[];
    colorFill(name: string): StyleOptionsColorFillValue;
    colorAngle(name: string): number;
    colorOrder(name: string): StyleOptionsColorOrderValue;
    /**
     * Picks the rotate/translateX/translateY/scale values for a single
     * component. Memoized per `name`, so the four values land in
     * {@link resolved} as `${name}Rotate` / `${name}TranslateX` /
     * `${name}TranslateY` / `${name}Scale` for downstream introspection.
     */
    componentTransform(name: string): {
        rotate: number;
        translateX: number;
        translateY: number;
        scale: number;
    };
    /**
     * Returns an informational snapshot of every value the resolver picked.
     * Includes top-level options (scale/rotate/translate/…), per-component
     * variants/probabilities/colors, and per-component transform picks. The
     * raw seed is deliberately excluded.
     *
     * The snapshot is NOT a round-trip-able options object — extra keys like
     * `${name}Rotate` are not part of {@link StyleOptions} and feeding the
     * snapshot back into a new {@link Avatar} is not supported. Callers that
     * need to reproduce an avatar should pass the original `seed` and
     * user-supplied options.
     *
     * The returned object aliases the internal cache; callers that need
     * isolation (e.g. {@link Avatar.toJSON}) clone it themselves.
     */
    resolved(): StyleOptions<D>;
}
