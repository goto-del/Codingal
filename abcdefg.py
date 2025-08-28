import tkinter as tk

def on_click(event):
    label1.config(text=f"Mouse clicked at {event.x}, {event.y}")
def on_key(event):
    label1.config(text=f"{event.char} pressed")

root = tk.Tk()
root.title("Events and Event Handlers")

root.geometry("400x300")

label1 = tk.Label(root, text="Click Me or press any key", bg="white", fg="black", font = ("Arial", 12))
label1.pack()

btn = tk.Button(root, text="Click Me!", bg="blue", font=("Arial", 12), fg="white")
btn.pack(pady=20)

root.bind("<Key>", on_key)
root.bind("<Button-1>", on_click)

root.mainloop()