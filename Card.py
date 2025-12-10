import tkinter as tk

def greet():
    name = e1.get()
    if name.strip() == "":
        greetlabel.config(text = "!! PLEASE ENTER YOUR NAME !!")
    else:
        greetlabel.config(text = f"Hello {name}. Welcome to Codingal.")

root = tk.Tk()
root.title("Greeting Card")
root.geometry("400x400")
root.config()

l1 = tk.Label(root, text="Enter your name", font = ("Arial", 14))
l1.pack(pady=10)

e1 = tk.Entry(root, width = 50, fg="blue")
e1.pack(pady=10)

b1 = tk.Button(root, text="Display Greetings", fg="White", bg="black", command=greet)
b1.pack(pady=10)

greetlabel = tk.Label(root, text="", font = ("Arial", 14))
greetlabel.pack(pady=10)


root.mainloop()