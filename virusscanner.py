from tkinter import*
from tkinter import messagebox

root = Tk()
root.geometry("400x300")


def msg():
    messagebox.askyesno( "Virus Scan", "Do you want to scan for viruses?")


button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)
button.pack()

root.mainloop()