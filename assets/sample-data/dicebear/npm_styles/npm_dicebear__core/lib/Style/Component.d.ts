import type { Range, StyleDefinitionComponent } from '../StyleDefinition.js';
import { ComponentTranslate } from './ComponentTranslate.js';
import { ComponentVariant } from './ComponentVariant.js';
/**
 * Read-only view over an entry in a style definition's `components` block.
 *
 * An entry is either a base component with its own dimensions and variants
 * or an alias declared via `extends`. Aliases are pure references — they
 * inherit dimensions, variants, and all transforms from the source.
 */
export declare class Component {
    #private;
    constructor(name: string, data: StyleDefinitionComponent, source?: Component);
    /**
     * Returns the entry's own name as declared in the style definition. For
     * aliases this is the alias key, not the source component's name (use
     * {@link sourceName} for the canonical user-option key prefix).
     */
    name(): string;
    /**
     * Returns the source component name when this entry is an alias, or
     * `undefined` for a base component.
     */
    extendsName(): string | undefined;
    /**
     * Returns the canonical user-option key prefix: the source component's
     * name when this entry is an alias, otherwise the entry's own name.
     */
    sourceName(): string;
    /**
     * Returns the component's intrinsic width in canvas coordinates. For
     * aliases the source component's width is returned.
     */
    width(): number;
    /**
     * Returns the component's intrinsic height in canvas coordinates. For
     * aliases the source component's height is returned.
     */
    height(): number;
    /**
     * Returns the probability (0–100) that this component is rendered.
     * Aliases delegate to the source; defaults to 100 (always visible).
     */
    probability(): number;
    /**
     * Returns the rotation range, or `undefined` when unset.
     * Aliases delegate to the source.
     */
    rotate(): Range | undefined;
    /**
     * Returns the scale range, or `undefined` when unset.
     * Aliases delegate to the source.
     */
    scale(): Range | undefined;
    /**
     * Returns the translate descriptor. Aliases delegate to the source.
     */
    translate(): ComponentTranslate;
    /**
     * Returns a name → {@link ComponentVariant} map for all defined variants.
     * Aliases delegate to the source component's variants.
     */
    variants(): ReadonlyMap<string, ComponentVariant>;
}
