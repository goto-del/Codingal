import tkinter as tk
from tkinter import messagebox, filedialog  

def open_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt" ), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = text_area.get(1.0, tk.END)
                file.write(content)
        messagebox.showinfo("Save File", "File saved successfully!")
def new_file():
    text_area.delete(1.0, tk.END)
root = tk.Tk()
root.title("Simple Text Editor")

root.geometry("750x500")

side_bar = tk.Frame(root,bg = "lightgrey", width=130)
side_bar.pack(side=tk.LEFT, fill=tk.Y)
open_button = tk.Button(side_bar, text="Open", command= open_file)
open_button.pack(pady=(30, 10), padx=20, fill=tk.X)
new_button = tk.Button(side_bar, text="New", command=new_file )
new_button.pack(pady=10, padx=20, fill=tk.X)
save_button = tk.Button(side_bar, text="Save",command= save_file)
save_button.pack(pady=10, padx=20, fill=tk.X)
text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 16))
text_area.pack(expand=True, fill=tk.BOTH)
root.mainloop()