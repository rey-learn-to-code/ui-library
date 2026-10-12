import type { Range, StyleDefinitionComponentTranslate } from '../StyleDefinition.js';
/**
 * Read-only view over a component's `translate` block, providing the X and Y
 * offset ranges.
 */
export declare class ComponentTranslate {
    #private;
    constructor(data: StyleDefinitionComponentTranslate);
    x(): Range | undefined;
    y(): Range | undefined;
}
