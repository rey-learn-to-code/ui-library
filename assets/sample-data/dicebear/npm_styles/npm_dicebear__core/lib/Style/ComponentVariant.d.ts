import type { StyleDefinitionComponentVariant } from '../StyleDefinition.js';
import { Element } from './Element.js';
/**
 * Read-only view over an entry in a component's `variants` block.
 */
export declare class ComponentVariant {
    #private;
    constructor(data: StyleDefinitionComponentVariant);
    /**
     * Returns the variant's elements, lazily wrapped as {@link Element}
     * instances on first access.
     */
    elements(): readonly Element[];
    /**
     * Returns the weighted-pick weight for this variant, defaulting to `1`.
     */
    weight(): number;
    /**
     * Returns the variant's descriptive tags (e.g. `hairLength:long`), or an
     * empty list when none are authored. Consumed by the `tags` render option
     * to filter the variant pool.
     */
    tags(): readonly string[];
    /**
     * Tests this variant against a single tag-filter token's grammar. With no
     * `value`, it matches a whole category: the bare `category` tag or any
     * `category:value` tag. With a `value`, it matches only the exact
     * `category:value` tag. The resolver composes these checks into the
     * allow/disallow filter structure.
     */
    hasTag(category: string, value?: string): boolean;
}
