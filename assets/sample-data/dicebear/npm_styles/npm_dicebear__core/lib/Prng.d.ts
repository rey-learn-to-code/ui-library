import type { Range } from './StyleDefinition.js';
/**
 * Key-based pseudorandom number generator.
 *
 * Each method takes a key that, combined with the seed, produces a
 * deterministic value. The same seed + key always yields the same result,
 * regardless of call order.
 */
export declare class Prng {
    #private;
    constructor(seed: string);
    /**
     * Picks a single item from `items` deterministically. Returns `undefined`
     * for an empty list. Duplicate values (by string representation) are
     * collapsed before picking so that input order and duplication do not
     * affect the result.
     */
    pick<T>(key: string, items: readonly T[]): T | undefined;
    /**
     * Picks a key from `weights` proportional to its weight. When all weights
     * are zero, falls back to an unweighted {@link pick}. Returns `undefined`
     * for an empty map.
     */
    weightedPick(key: string, weights: Readonly<Record<string, number>>): string | undefined;
    /**
     * Returns `true` with the given probability (0–100, default 50).
     */
    bool(key: string, likelihood?: number): boolean;
    /**
     * Returns a deterministic float in `range`, rounded to four decimal places.
     * With `range.step > 0`, the result is drawn uniformly from
     * `{ min + i*step | 0 ≤ i ≤ floor((max - min) / step) }`, so both endpoints
     * of an evenly-divisible range are equally likely. Non-positive or absent
     * step means continuous. `min`/`max` are sorted internally, so a reversed
     * pair is tolerated.
     */
    float(key: string, range: Range): number;
    /**
     * Returns a deterministic integer in `range`. `min`/`max` are sorted
     * internally, so a reversed pair is tolerated. `range.step` is accepted
     * for symmetry with {@link float} but ignored — integers already step by 1.
     */
    integer(key: string, range: Range): number;
    /**
     * Fisher-Yates shuffle with chained Mulberry32 state. Duplicate values
     * (by string representation) are collapsed before shuffling, so a
     * caller's slice off the front cannot accidentally produce a repeated
     * value.
     */
    shuffle<T>(key: string, items: readonly T[]): T[];
    /**
     * Returns a single float in `[0, 1)` derived from `seed:key`. The same
     * seed/key pair always produces the same value.
     */
    getValue(key: string): number;
}
