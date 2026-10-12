import type { StyleDefinitionElement, StyleDefinitionElementValue, StyleDefinitionElementType, StyleDefinitionAttributes } from '../StyleDefinition.js';
/**
 * Read-only view over a single render-tree element from a style definition.
 *
 * The same node type covers SVG elements, text, and component references —
 * `type()` discriminates between them.
 */
export declare class Element {
    #private;
    constructor(data: StyleDefinitionElement);
    /**
     * Returns the element type discriminator (`svg`, `text`, `component`, …).
     */
    type(): StyleDefinitionElementType;
    /**
     * Returns the element's tag/component name, or `undefined` for elements
     * that don't have one.
     */
    name(): string | undefined;
    /**
     * Returns the element's textual value (for `text` elements) or template
     * fragment, or `undefined` when not applicable.
     */
    value(): StyleDefinitionElementValue | undefined;
    /**
     * Returns the element's raw attribute map, or `undefined` when no
     * attributes are defined.
     */
    attributes(): StyleDefinitionAttributes | undefined;
    /**
     * Returns the element's children, lazily wrapped as {@link Element}
     * instances on first access.
     */
    children(): readonly Element[];
}
