/**
 * 1. Function to calculate the sum of any number of arguments.
 * We use the rest parameter (...args) to collect all arguments into an array.
 */
function sumArguments(...args) {
    let sum = 0;
    for (let i = 0; i < args.length; i++) {
        // Ensure we are adding numbers
        if (typeof args[i] === 'number') {
            sum += args[i];
        }
    }
    return sum;
}

/**
 * 2. Function to print the values of trigonometric functions for a given degree.
 * Note: JavaScript's Math.sin, Math.cos, and Math.tan expect radians, not degrees.
 * So we must convert degrees to radians first: radians = degrees * (Math.PI / 180)
 */
function printTrigonometricValues(degree) {
    const radians = degree * (Math.PI / 180);

    const sineValue = Math.sin(radians);
    const cosineValue = Math.cos(radians);
    const tangentValue = Math.tan(radians);

    console.log(`--- Trigonometric Values for ${degree}° ---`);
    console.log(`Sine   (${degree}°): ${sineValue.toFixed(4)}`);
    console.log(`Cosine (${degree}°): ${cosineValue.toFixed(4)}`);
    
    // Handle tangent for 90 degrees which approaches infinity
    if (degree === 90 || degree === 270) {
        console.log(`Tangent(${degree}°): Infinity (or undefined)`);
    } else {
        console.log(`Tangent(${degree}°): ${tangentValue.toFixed(4)}`);
    }
    console.log("------------------------------------\n");
}

// ==========================================
// Executing and Testing the functions
// ==========================================

console.log("====================================");
console.log("       SUM OF ARGUMENTS TESTS       ");
console.log("====================================\n");

console.log(`Result of sumArguments(5, 10, 15): ${sumArguments(5, 10, 15)}`);
console.log(`Result of sumArguments(1, 2, 3, 4, 5): ${sumArguments(1, 2, 3, 4, 5)}`);
console.log(`Result of sumArguments(100, -50, 25): ${sumArguments(100, -50, 25)}`);
console.log("\n");

console.log("====================================");
console.log("     TRIGONOMETRIC VALUES TESTS     ");
console.log("====================================\n");

// Array of common degrees to test
const degreesToTest = [0, 30, 45, 60, 90];

degreesToTest.forEach(degree => {
    printTrigonometricValues(degree);
});
