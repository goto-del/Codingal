import tkinter as tk

def another():
    wow = tk.Toplevel()
    wow.title("Another One")
    wow.geometry("150x150")

    l3 = tk.Label(wow, text="YOU DID IT!")
    l3.pack(pady=10)

    wow.mainloop()
def opening():
    top = tk.Toplevel()
    top.title("A Window")
    top.geometry("250x250")

    l2 = tk.Label(top, text="This is A top Level Window.")
    l2.pack(pady=10)

    b2 = tk.Button(top, text="Don't Click Me Or else another one will come", command=another)
    b2.pack(pady=10)

    top.mainloop()

root = tk.Tk()
root.title("Top A Window")
root.geometry("350x350")


label1 = tk.Label(root, text="This is a root window.")
label1.pack(pady=10)

button1 = tk.Button(root, text="Click here to open another window.", command=opening)
button1.pack(pady=10)

root.mainloop()