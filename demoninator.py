import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Denomination Calculator")
root.config(bg="#514bec")
root.geometry("650x400")
root.resizable(False, False)

# Load and resize image
image = Image.open("Happy.jpg")
image = image.resize((300, 300))
ing = ImageTk.PhotoImage(image)

# UI labels
label1 = tk.Label(root, image=ing)
label1.place(x=180, y=20)
label1 = tk.Label(root, text="Denomination Calculator", font=("Arial", 20, "bold"),
                  bg="#656491", fg="white")
label1.place(relx=0.5, y=345, anchor="center")

# Open Top Window
def msg():
    m = messagebox.showinfo("ALERT", "Do you want to calculate denomination?")
    if m == "ok":
        topwin()

def topwin():
    top = tk.Toplevel()
    top.title("Denomination Calculator")
    top.config(bg="#4bec5b")
    top.geometry("600x400+50+50")
    top.resizable(False, False)

    label2 = tk.Label(top, text="Enter total amount: ", font=("Arial", 12, "bold"),
                      bg="#522ad6", fg="white")
    label2.place(x=230, y=50)

    entry = tk.Entry(top, font=("Arial", 12, "bold"), bg="#d6a522", fg="white")
    entry.place(x=200, y=80)

    lbl = tk.Label(top, text="Here are the number of notes for each denomination",
                   font=("Arial", 12, "bold"), bg="#e94bec", fg="white")
    lbl.place(x=80, y=170)

    # Labels
    l1 = tk.Label(top, text="2000", bg='light grey')
    l2 = tk.Label(top, text="500", bg='light grey')
    l3 = tk.Label(top, text="100", bg='light grey')
    l4 = tk.Label(top, text="10", bg='light grey')
    l5 = tk.Label(top, text="1", bg='light grey')

    # Entry fields
    t1 = tk.Entry(top)
    t2 = tk.Entry(top)
    t3 = tk.Entry(top)
    t4 = tk.Entry(top)
    t5 = tk.Entry(top)

    # Place them properly
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    l4.place(x=180, y=290)
    l5.place(x=180, y=320)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    t4.place(x=270, y=290)
    t5.place(x=270, y=320)

    # Calculate function inside topwin so it has access to widgets
    def calculate():
        try:
            amount = int(entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return

        n2000 = amount // 2000
        amount %= 2000
        n500 = amount // 500
        amount %= 500
        n100 = amount // 100
        amount %= 100
        n10 = amount // 10
        amount %= 10
        n1 = amount // 1

        # clear and insert values
        for box in (t1, t2, t3, t4, t5):
            box.delete(0, tk.END)

        t1.insert(0, str(n2000))
        t2.insert(0, str(n500))
        t3.insert(0, str(n100))
        t4.insert(0, str(n10))
        t5.insert(0, str(n1))

    # Button connected to calculate()
    button2 = tk.Button(top, text="Calculate", font=("Arial", 12, "bold"),
                        bg="#2e8540", fg="white", command=calculate)
    button2.place(x=240, y=140)

# Main button
button1 = tk.Button(root, text="Let's get started", font=("Arial", 12, "bold"),
                    bg="#AC4444", fg="white", command=msg)
button1.place(x=260, y=360)

root.mainloop()