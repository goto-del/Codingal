// Initialize count
let count = 0;

// Select the value display and all buttons
const value = document.getElementById("value");
const btns = document.querySelectorAll(".btn");

// Loop over each button
btns.forEach(function (btn) {
    btn.addEventListener("click", function (e) {
        // Check classes of the clicked button
        const styles = e.currentTarget.classList;
        
        // Update the count variable
        if (styles.contains("decrease")) {
            count--;
        } else if (styles.contains("increase")) {
            count++;
        } else {
            count = 0;
        }

        // Change the text color based on the value
        if (count > 0) {
            value.style.color = "var(--success-color)";
        } else if (count < 0) {
            value.style.color = "var(--danger-color)";
        } else {
            value.style.color = "var(--dark-color)";
        }

        // Display the updated count
        value.textContent = count;
    });
});
