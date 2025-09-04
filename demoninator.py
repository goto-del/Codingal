import tkinter as tk
from tkinter import messagebox
from PIL import Image  , ImageTk

root = tk.Tk()
root.title("Denomination Calculator")
root.config(bg = "#514bec")
root.geometry("650x400")
root.resizable(False, False)

image = Image.open("Happy.jpg")
image = image.resize((300, 300))

ing = ImageTk.PhotoImage(image)
label1 = tk.Label(root , image = ing)
label1.place(x = 180, y = 20)
label1 = tk.Label(root, text= "Denomination Calculator", font=("Arial", 20, "bold"), bg="#656491", fg="white")
label1.place(relx = 0.5, y = 345, anchor = "center")
def msg():
    m = messagebox.showinfo("ALERT", "Do you want to calculate denomination?")
    if m == "ok":
        topwin()



button1 = tk.Button(root, text="Let's get started", font=("Arial", 12, "bold"), bg="#AC4444", fg="white", command=msg)

button1.place(x = 260, y = 360)

def topwin():
    top = tk.Toplevel()
    top.title("Denomination Calculator")
    top.config(bg = "#4bec5b")
    top.geometry("600x350+50+50")
    top.resizable(False, False)
    label2 = tk.Label(top, text="End up total amount: ", font=("Arial", 12, "bold"), bg="#522ad6", fg="white")
    label2.place(x = 230, y = 50)
    entry = tk.Entry(top, font=("Arial", 12, "bold"), bg="#d6a522", fg="white")
    entry.place(x = 200, y = 80)
    button2 = tk.Button(top, text="Calculate", font=("Arial", 12, "bold"), bg="#2e8540", fg="white")
    button2.place(x = 240, y = 140)
    lbl = tk.Label(top, text="Here are the number of notes for each denomination", font=("Arial", 12, "bold"), bg="#e94bec", fg="white")
    lbl.place(x = 140, y = 170)
    l1 = tk.Label(top, text="2000", bg='light grey')

    l2 = tk.Label(top, text="500", bg='light grey')

    l3 = tk.Label(top, text="100", bg='light grey')

    t1 = tk.Entry(top)

    t2 = tk.Entry(top)

    t3 = tk.Entry(top)

    l1.place(x = 180, y = 200)
    l2.place(x = 180, y = 230)
    l3.place(x = 180, y = 260)
    t1.place(x = 270, y = 200)
    t2.place(x = 270, y = 230)
    t3.place(x = 270, y = 260)
    
root.mainloop()