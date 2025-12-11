import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Display Example")

image = Image.open("WIN_20250610_12_38_26_Pro.jpg")
image = image.resize((400,301))

photo = ImageTk.PhotoImage(image)

imagelabel = tk.Label(root, image=photo)
imagelabel.pack(pady=10)

label = tk.Label(root, text="This is a Image", font = ("Arial", 14))
label.pack(pady=10)




root.mainloop()