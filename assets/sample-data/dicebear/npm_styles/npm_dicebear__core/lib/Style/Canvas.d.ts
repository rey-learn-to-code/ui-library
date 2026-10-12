import type { StyleDefinitionCanvas } from '../StyleDefinition.js';
import { Element } from './Element.js';
/**
 * Read-only view over a style definition's `canvas` block, exposing the
 * drawing area dimensions and the top-level element list.
 */
export declare class Canvas {
    #private;
    constructor(data: StyleDefinitionCanvas);
    /**
     * Returns the canvas width — the `width` value of the SVG `viewBox`.
     */
    width(): number;
    /**
     * Returns the canvas height — the `height` value of the SVG `viewBox`.
     */
    height(): number;
    /**
     * Returns the top-level elements rendered onto the canvas, lazily wrapped
     * as {@link Element} instances on first access.
     */
    elements(): readonly Element[];
}
