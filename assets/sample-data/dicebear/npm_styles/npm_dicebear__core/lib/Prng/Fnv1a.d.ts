/**
 * FNV-1a 32-bit hash.
 *
 * Offset basis: 0x811c9dc5, prime: 0x01000193.
 *
 * @see https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
 */
export declare class Fnv1a {
    /**
     * Returns the unsigned 32-bit FNV-1a hash of `input`. UTF-16 code units
     * are hashed directly so the result is identical across language ports.
     */
    static hash(input: string): number;
    /**
     * Returns the FNV-1a hash of `input` as an 8-character lowercase hex string.
     */
    static hex(input: string): string;
}
