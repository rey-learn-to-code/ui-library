import type { StyleDefinitionMeta } from '../StyleDefinition.js';
import { MetaLicense } from './MetaLicense.js';
import { MetaCreator } from './MetaCreator.js';
import { MetaSource } from './MetaSource.js';
/**
 * Lazily-constructed view over a style definition's `meta` block, exposing
 * the license, creator, and source descriptors.
 */
export declare class Meta {
    #private;
    constructor(data: StyleDefinitionMeta);
    /**
     * Returns the license descriptor, defaulting to an empty object when the
     * style definition omits the field.
     */
    license(): MetaLicense;
    /**
     * Returns the creator descriptor, defaulting to an empty object when the
     * style definition omits the field.
     */
    creator(): MetaCreator;
    /**
     * Returns the source descriptor, defaulting to an empty object when the
     * style definition omits the field.
     */
    source(): MetaSource;
}
