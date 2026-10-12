import { ValidationError } from './ValidationError.js';
import type { ValidationErrorDetail } from './ValidationError.js';
/**
 * Thrown when a style definition fails schema validation.
 */
export declare class StyleValidationError extends ValidationError {
    constructor(details: readonly ValidationErrorDetail[]);
}
