import type { StyleDefinitionMetaCreator } from '../StyleDefinition.js';
/**
 * Read-only view over the `meta.creator` block of a style definition.
 */
export declare class MetaCreator {
    #private;
    constructor(data: StyleDefinitionMetaCreator);
    /**
     * Returns the creator's display name, or `undefined` when not set.
     */
    name(): string | undefined;
    /**
     * Returns the creator's homepage URL, or `undefined` when not set.
     */
    url(): string | undefined;
}
