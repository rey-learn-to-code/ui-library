import type { StyleDefinition, StyleDefinitionAttributes } from './StyleDefinition.js';
import { Meta } from './Style/Meta.js';
import { Canvas } from './Style/Canvas.js';
import { Component } from './Style/Component.js';
import { Color } from './Style/Color.js';
export type { StyleDefinition } from './StyleDefinition.js';
/**
 * Validated, lazily-decomposed wrapper around a style definition. Construction
 * runs the JSON Schema validator and stores a deep clone of the input so that
 * later mutation of the source object cannot leak into the rendered avatar.
 */
export declare class Style<D = unknown> {
    #private;
    constructor(data: D);
    /**
     * Returns the definition's `$id`, or `undefined` when not set.
     */
    id(): string | undefined;
    /**
     * Returns the definition's `$schema` URI, or `undefined` when not set.
     */
    schema(): string | undefined;
    /**
     * Returns the definition's `$comment`, or `undefined` when not set.
     */
    comment(): string | undefined;
    /**
     * Returns the {@link Meta} view, lazily constructed on first access.
     */
    meta(): Meta;
    /**
     * Returns a deep clone of the root SVG attributes from the definition,
     * defaulting to an empty object.
     */
    attributes(): StyleDefinitionAttributes;
    /**
     * Returns a deep clone of the underlying definition.
     */
    definition(): StyleDefinition;
    /**
     * Returns the {@link Canvas} view, lazily constructed on first access.
     */
    canvas(): Canvas;
    /**
     * Returns a name → {@link Component} map for all defined components, built
     * lazily on first access.
     */
    components(): ReadonlyMap<string, Component>;
    /**
     * Returns a name → {@link Color} map for all defined colors, built lazily
     * on first access.
     */
    colors(): ReadonlyMap<string, Color>;
}
