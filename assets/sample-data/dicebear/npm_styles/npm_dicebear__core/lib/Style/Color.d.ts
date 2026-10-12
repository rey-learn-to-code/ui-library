import type { StyleDefinitionColor } from '../StyleDefinition.js';
/**
 * Read-only view over an entry in a style definition's `colors` block.
 */
export declare class Color {
    #private;
    constructor(data: StyleDefinitionColor);
    /**
     * Returns the candidate color values, in definition order.
     */
    values(): readonly string[];
    /**
     * Returns the colors that the resolver should avoid picking, or an empty
     * list when the field is unset.
     */
    notEqualTo(): readonly string[];
    /**
     * Returns the name of another color that this one should contrast against,
     * or `undefined` when no contrast constraint is defined.
     */
    contrastTo(): string | undefined;
}
