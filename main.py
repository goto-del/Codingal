import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

menu = [ 
    {"Item": "Piza", "Price": 250.00},
    {"Item": "Burger", "Price": 150.00},
    {"Item": "Pasta", "Price": 200.00},
    {"Item": "Sandwich", "Price": 100.00},
    {"Item": "Coffee", "Price": 50.00},
    {"Item": "Tea", "Price": 40.00},
    {"Item": "Juice", "Price": 20.00}
 ]

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Menu")
        self.root.geometry("600x500")
        
        bg_image = Image.open("bg.jpeg")
        bg_image = bg_image.resize((600, 500))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=self.bg_photo)
        bg_label.place(x = 0, y = 0, relwidth=1, relheight=1)

        menu_frame = tk.Frame(root, bg="white", bd=5)
        menu_frame.place(relx=0.5, rely=0.5, anchor = "center")
        tk.Label(menu_frame, text="Menu", font=("Arial", 18, "bold") bg="white".grid(row=0, column=0,columnspan=3, pady=10))
