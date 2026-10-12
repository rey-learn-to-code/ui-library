export type StyleOptionsFlipValue = 'none' | 'horizontal' | 'vertical' | 'both';
export type StyleOptionsColorFillValue = 'solid' | 'linear' | 'radial';
export type StyleOptionsColorOrderValue = 'random' | 'fixed';
export declare const COLOR_ORDER_RANDOM: StyleOptionsColorOrderValue;
export declare const COLOR_ORDER_FIXED: StyleOptionsColorOrderValue;
/**
 * A parsed `tags` filter token. {@link Options.tags} decodes each raw
 * `category` / `category:value` / `!…` string into this shape so the resolver
 * composes the filter without parsing the grammar itself.
 */
export interface TagFilterToken {
    readonly category: string;
    readonly value?: string;
    readonly negated: boolean;
}
type ComponentNames<D> = D extends {
    components: Record<infer K extends string, unknown>;
} ? string extends K ? never : K : never;
type ColorNames<D> = D extends {
    colors: Record<infer K extends string, unknown>;
} ? string extends K ? never : K : never;
type AllColorNames<D> = ColorNames<D> | 'background';
type ResolveComponent<D, C extends string> = D extends {
    components: Record<string, unknown>;
} ? C extends keyof D['components'] ? D['components'][C] extends {
    extends: infer P extends string;
} ? P extends keyof D['components'] ? D['components'][P] : never : D['components'][C] : never : never;
type VariantNames<D, C extends string> = ResolveComponent<D, C> extends {
    variants: Record<infer V extends string, unknown>;
} ? string extends V ? string : V : string;
type HasSpecificKeys<D> = [ComponentNames<D>] extends [never] ? [ColorNames<D>] extends [never] ? false : true : true;
export interface StyleOptionsBase {
    readonly seed?: string;
    readonly size?: number;
    readonly idRandomization?: boolean;
    readonly title?: string;
    readonly flip?: StyleOptionsFlipValue | readonly StyleOptionsFlipValue[];
    readonly fontFamily?: string | readonly string[];
    readonly fontWeight?: number | readonly number[];
    readonly scale?: number | readonly [number, number];
    readonly borderRadius?: number | readonly [number, number];
    readonly rotate?: number | readonly [number, number];
    readonly translateX?: number | readonly [number, number];
    readonly translateY?: number | readonly [number, number];
    readonly tags?: string | readonly string[];
}
type ComponentVariantOption<D, K extends string> = VariantNames<D, K> | readonly VariantNames<D, K>[] | Readonly<Partial<Record<VariantNames<D, K>, number>>>;
type IsAlias<D, C extends string> = D extends {
    components: Record<string, unknown>;
} ? C extends keyof D['components'] ? D['components'][C] extends {
    extends: string;
} ? true : false : false : false;
type ComponentOptions<D, C extends string> = [C] extends [never] ? unknown : {
    readonly [K in C as IsAlias<D, K> extends true ? never : `${K}Variant`]?: ComponentVariantOption<D, K>;
} & {
    readonly [K in C as IsAlias<D, K> extends true ? never : `${K}Probability`]?: number;
};
type ColorOptions<C extends string> = [C] extends [never] ? unknown : {
    readonly [K in C as `${K}Color`]?: string | readonly string[];
} & {
    readonly [K in C as `${K}ColorFill`]?: StyleOptionsColorFillValue | readonly StyleOptionsColorFillValue[];
} & {
    readonly [K in C as `${K}ColorFillStops`]?: number | readonly [number, number];
} & {
    readonly [K in C as `${K}ColorAngle`]?: number | readonly [number, number];
} & {
    readonly [K in C as `${K}ColorOrder`]?: StyleOptionsColorOrderValue;
};
export type StyleOptions<D = unknown> = StyleOptionsBase & ComponentOptions<D, ComponentNames<D>> & ColorOptions<AllColorNames<D>> & (HasSpecificKeys<D> extends true ? unknown : {
    readonly [key: string]: unknown;
});
export {};
