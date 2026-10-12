import type { StyleDefinitionMetaLicense } from '../StyleDefinition.js';
/**
 * Read-only view over the `meta.license` block of a style definition.
 */
export declare class MetaLicense {
    #private;
    constructor(data: StyleDefinitionMetaLicense);
    /**
     * Returns the license name (e.g. `"CC BY 4.0"`), or `undefined` when not set.
     */
    name(): string | undefined;
    /**
     * Returns the license URL, or `undefined` when not set.
     */
    url(): string | undefined;
    /**
     * Returns the full license text, or `undefined` when not set.
     */
    text(): string | undefined;
}
