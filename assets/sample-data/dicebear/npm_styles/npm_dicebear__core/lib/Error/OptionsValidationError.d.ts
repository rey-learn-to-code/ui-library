import { ValidationError } from './ValidationError.js';
import type { ValidationErrorDetail } from './ValidationError.js';
/**
 * Thrown when avatar options fail schema validation.
 */
export declare class OptionsValidationError extends ValidationError {
    constructor(details: readonly ValidationErrorDetail[]);
}
