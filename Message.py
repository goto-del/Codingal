import tkinter as tk
from tkinter import messagebox

def scan():
    messagebox.showwarning(title="ALERT", message="VIRUS FOUND")

root = tk.Tk()
root.title("Virus Scanner")
root.geometry("350x350")

button1 = tk.Button(root, text="Scan for Virus", fg = "white", bg="green", command=scan)
button1.pack(pady=10)




root.mainloop()