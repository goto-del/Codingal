import tkinter as tk

def on_click(event):
    label1.config(text=f"Answer is ", * 2.54)

root = tk.Tk()
root.title("Length Converter app")
root.geometry("400x400")

label1 = tk.Label(root, text="Enter length in inches", bg="white", fg="black", font = ("Arial", 12))
label1.pack()

btn = tk.Button(root, text="I am the converter I will convert the inches to centimeters", bg="blue", font=("Arial", 12), fg="white")
btn.pack(pady=20)

root.bind("<Button-1>", on_click)


root.mainloop()