import tkinter as tk

def cal():
    amount = int(e1.get())
    note2000 = amount // 2000
    amount = amount%2000
    note500 = amount // 500
    amount =  amount%500
    note100 = amount // 100
    amount = amount%100
    note1 = amount // 1


    result.config(text=f"₹2,000 notes : {note2000}\n ₹500 notes : {note500}\n ₹100 notes : {note100}\n ₹1 notes : {note1}\n")
    
    

root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("300x300")


l1 = tk.Label(root ,text="Enter the Amount in Rupees", font = ("Arial", 13))
l1.pack(pady=10)

e1 = tk.Entry(root, width=200)
e1.pack(pady=10)

b1 = tk.Button(root, text="Calculate", fg = "white", bg="black", command=cal)
b1.pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 15))
result.pack(pady=10)

root.mainloop()