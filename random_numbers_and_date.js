// JavaScript Program: Random Numbers and Date
// This program demonstrates the use of built-in methods (Math, Date) and loops.

console.log("=========================================");
console.log("          CURRENT DATE AND TIME          ");
console.log("=========================================\n");

// 1. Getting and printing the current date using the built-in Date object
const currentDate = new Date();
console.log("The current date and time is:");
console.log(currentDate.toString());
// Alternatively, formatting it specifically:
// console.log(currentDate.toLocaleString());
console.log("\n");


console.log("=========================================");
console.log("      RANDOM SET OF NUMBERS (LOOP)       ");
console.log("=========================================\n");

// 2. Printing a random set of numbers using a loop
const count = 5; // We will generate 5 random numbers
console.log(`Generating ${count} random numbers (between 0 and 100):`);

for (let i = 1; i <= count; i++) {
    // Math.random() generates a decimal between 0 and 1. 
    // Multiplying by 100 scales it to be between 0 and 100.
    let randomNum = Math.random() * 100;
    console.log(`Number ${i}: ${randomNum}`);
}
console.log("\n");


console.log("=========================================");
console.log("         ROUNDED RANDOM NUMBER           ");
console.log("=========================================\n");

// 3. Printing a rounded random number
// Generate a new random number
let rawRandomNumber = Math.random() * 50; // Random number between 0 and 50

// Use the built-in Math.round() method to round to the nearest integer
let roundedNumber = Math.round(rawRandomNumber);

// You can also use Math.floor() to round down or Math.ceil() to round up.
let flooredNumber = Math.floor(rawRandomNumber);
let ceiledNumber = Math.ceil(rawRandomNumber);

console.log(`Raw Random Number:  ${rawRandomNumber}`);
console.log(`Rounded (Nearest):  ${roundedNumber}`);
console.log(`Rounded Down:       ${flooredNumber}`);
console.log(`Rounded Up:         ${ceiledNumber}`);
console.log("\n=========================================");
