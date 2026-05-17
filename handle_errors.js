// Example of handling errors in JavaScript using try...catch

function divideNumbers(a, b) {
    if (b === 0) {
        // We manually create and throw an error if the user tries to divide by zero
        throw new Error("Division by zero is not allowed.");
    }
    return a / b;
}

console.log("--- Starting Error Handling Demonstration ---\n");

try {
    // This part of the code might throw an error
    
    // This first call will work perfectly fine
    let validResult = divideNumbers(10, 2);
    console.log("Result of 10 / 2 is:", validResult);
    
    console.log("\nAttempting to divide by 0...");
    
    // This next line will throw the Error we defined in the function
    let invalidResult = divideNumbers(10, 0);
    
    // Since an error was thrown above, this next line will NEVER execute
    console.log("This line will never be reached because the program jumps to 'catch'.");
    
} catch (error) {
    // The catch block intercepts the error so the program doesn't crash
    console.log("\n❌ [ERROR CAUGHT!] The program intercepted an issue.");
    console.log("Details of the error:", error.message);
    
} finally {
    // The finally block ALWAYS executes, whether there was an error or not.
    // It's typically used for cleaning up resources.
    console.log("\n--- Finally block execution ---");
    console.log("The try...catch structure has completed.");
}
