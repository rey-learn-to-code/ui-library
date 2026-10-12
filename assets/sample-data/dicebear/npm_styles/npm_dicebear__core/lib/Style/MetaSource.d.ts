import type { StyleDefinitionMetaSource } from '../StyleDefinition.js';
/**
 * Read-only view over the `meta.source` block of a style definition.
 */
export declare class MetaSource {
    #private;
    constructor(data: StyleDefinitionMetaSource);
    /**
     * Returns the source name (e.g. the original work title), or `undefined`
     * when not set.
     */
    name(): string | undefined;
    /**
     * Returns the URL of the source, or `undefined` when not set.
     */
    url(): string | undefined;
}
