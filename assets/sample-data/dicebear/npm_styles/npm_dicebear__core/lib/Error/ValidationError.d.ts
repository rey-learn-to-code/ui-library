export interface ValidationErrorDetail {
    readonly message?: string;
    readonly instancePath?: string;
    /** JSON pointer to the schema rule that failed, e.g. `#/properties/size/minimum`. */
    readonly schemaPath?: string;
    /** The failing schema keyword, e.g. `minimum` or `pattern`. */
    readonly keyword?: string;
}
/**
 * Base class for schema validation errors. Carries the prefix in `message`
 * and the per-field failures in {@link details}.
 */
export declare class ValidationError extends Error {
    readonly details: readonly ValidationErrorDetail[];
    constructor(prefix: string, details: readonly ValidationErrorDetail[]);
}
