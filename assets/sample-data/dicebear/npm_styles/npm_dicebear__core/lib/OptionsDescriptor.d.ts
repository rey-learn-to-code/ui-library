import type { Style } from './Style.js';
interface StringField {
    readonly type: 'string';
    readonly list?: true;
}
interface NumberField {
    readonly type: 'number';
    readonly min?: number;
    readonly max?: number;
    readonly list?: true;
}
interface BooleanField {
    readonly type: 'boolean';
}
interface EnumField {
    readonly type: 'enum';
    readonly values: readonly string[];
    readonly list?: true;
    readonly weighted?: true;
    readonly open?: true;
}
interface ColorField {
    readonly type: 'color';
    readonly list?: true;
    readonly contrastTo?: string;
    readonly notEqualTo?: readonly string[];
}
interface RangeField {
    readonly type: 'range';
    readonly min?: number;
    readonly max?: number;
}
export type FieldDescriptor = StringField | NumberField | BooleanField | EnumField | ColorField | RangeField;
export type Descriptor = Record<string, FieldDescriptor>;
/**
 * Builds a descriptor of every option a given style accepts. Tooling such as
 * the editor uses the result to render form controls and validation hints
 * without having to introspect the style itself.
 */
export declare class OptionsDescriptor {
    #private;
    constructor(style: Style);
    /**
     * Returns a deep clone of the descriptor, building it lazily on first call.
     */
    toJSON(): Descriptor;
}
export {};
