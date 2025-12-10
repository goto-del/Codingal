import tkinter as tk

root = tk.Tk()
root.title("Simple Tk program")
root.geometry("400x300")
root.config(bg = "lightblue")

l1 = tk.Label(root, text="Hello User!", bg = "lightblue", font = ("Arial", 16))
l1.pack(pady=10)

b1 = tk.Button(root, text = "CLICK ME!", bg="black", fg="white")
b1.pack(pady=10)

e1 = tk.Entry(root, fg="blue", width = 50)
e1.pack(pady=10)

f1 = tk.Frame(root, relief="raised", borderwidth=5)
f1.pack(pady=10)

l2 = tk.Label(f1, text="Sample Frame")
l2.pack(pady=10)

t1 = tk.Text(root, fg = "green", bg="yellow")
t1.pack(pady=10)

root.mainloop()