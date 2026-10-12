/**
 * Derives display initials from a seed string.
 *
 * @see https://www.regular-expressions.info/unicode.html
 */
export declare class Initials {
    /**
     * Returns one or two uppercase initials for the given seed. By default
     * strips `@...` so email addresses yield a single initial instead of being
     * treated as two words.
     */
    static fromSeed(seed: string, discardAtSymbol?: boolean): string;
}
