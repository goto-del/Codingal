import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        # Retrieve the values from the input fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        # Calculate the product
        result = num1 * num2
        
        # Update the label to display the product
        result_label.config(text=f"Product: {result}", fg="blue")
    except ValueError:
        # Show an error message if the user enters text or leaves it blank
        messagebox.showerror("Input Error", "Please enter valid numbers in both fields.")

# Initialize the main Tkinter window
app = tk.Tk()
app.title("Product Calculator")
app.geometry("350x250")
app.configure(padx=20, pady=20)

# Title Label
title_label = tk.Label(app, text="Find the Product", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 15))

# --- Number 1 Input ---
frame1 = tk.Frame(app)
frame1.pack(fill="x", pady=5)
label_num1 = tk.Label(frame1, text="Enter First Number: ", font=("Arial", 10))
label_num1.pack(side="left")
entry_num1 = tk.Entry(frame1, font=("Arial", 10))
entry_num1.pack(side="right", expand=True, fill="x")

# --- Number 2 Input ---
frame2 = tk.Frame(app)
frame2.pack(fill="x", pady=5)
label_num2 = tk.Label(frame2, text="Enter Second Number: ", font=("Arial", 10))
label_num2.pack(side="left")
entry_num2 = tk.Entry(frame2, font=("Arial", 10))
entry_num2.pack(side="right", expand=True, fill="x")

# --- Calculate Button ---
calculate_btn = tk.Button(app, text="Calculate Product", command=calculate_product, 
                          bg="#0078D7", fg="white", font=("Arial", 11, "bold"), cursor="hand2")
calculate_btn.pack(pady=15, fill="x")

# --- Result Label ---
result_label = tk.Label(app, text="Product: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

# Run the Tkinter event loop
if __name__ == "__main__":
    app.mainloop()
