/**
 * Mulberry32 PRNG — stateful, matching the C reference by Tommy Ettinger.
 *
 * C original:
 * ```c
 * uint32_t z = (x += 0x6D2B79F5UL);
 * z = (z ^ (z >> 15)) * (z | 1UL);
 * z ^= z + (z ^ (z >> 7)) * (z | 61UL);
 * return z ^ (z >> 14);
 * ```
 *
 * @see https://gist.github.com/tommyettinger/46a874533244883189143505d203312c
 */
export declare class Mulberry32 {
    #private;
    constructor(seed: number);
    /**
     * Advances the state and returns the next unsigned 32-bit value.
     */
    next(): number;
    /**
     * Advances the state and returns the next value in `[0, 1)`.
     */
    nextFloat(): number;
    /**
     * Returns the current internal state, useful for snapshotting.
     */
    state(): number;
}
