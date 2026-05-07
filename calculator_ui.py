import tkinter as tk
from tkinter import font

def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate the x and y coordinates to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the dimensions of the screen and where it is placed
    window.geometry(f'{width}x{height}+{x}+{y}')

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

def show_owner_page():
    calc_frame.pack_forget()
    owner_frame.pack(fill=tk.BOTH, expand=True)

def show_calc_page():
    owner_frame.pack_forget()
    calc_frame.pack(fill=tk.BOTH, expand=True)

window = tk.Tk()
window.title("Calculator")
window.resizable(0, 0)
# Increased height from 520 to 580 to ensure the Owner button is fully visible
center_window(window, 340, 580)

# Colors - sleek, minimalist dark theme (not colorful)
BG_COLOR = "#1e1e1e"
BTN_BG = "#2d2d2d"
BTN_FG = "#ffffff"
BTN_ACTIVE_BG = "#3d3d3d"
BTN_HIGHLIGHT = "#404040"

window.configure(bg=BG_COLOR)

expression = ""
input_text = tk.StringVar()

# --- Calc Frame ---
calc_frame = tk.Frame(window, bg=BG_COLOR)
calc_frame.pack(fill=tk.BOTH, expand=True)

# Input field frame (Packed Top)
input_frame = tk.Frame(calc_frame, bg=BG_COLOR)
input_frame.pack(side=tk.TOP, fill=tk.X, padx=15, pady=25)

input_field = tk.Entry(input_frame, font=('Segoe UI', 32), textvariable=input_text, bg=BG_COLOR, fg=BTN_FG, bd=0, justify=tk.RIGHT, insertbackground=BTN_FG)
input_field.pack(fill=tk.X, ipady=10)

# Owner button (Packed Bottom, before btns_frame so it stays pinned)
owner_btn = tk.Button(calc_frame, text="Owner", font=('Segoe UI', 12), fg=BTN_FG, bg=BTN_HIGHLIGHT, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, bd=0, cursor="hand2", command=show_owner_page)
owner_btn.pack(side=tk.BOTTOM, fill=tk.X, padx=13, pady=15, ipady=8)

# Buttons frame (Packed Top, fills remaining space)
btns_frame = tk.Frame(calc_frame, bg=BG_COLOR)
btns_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

def create_button(text, r, c, col_span=1, bg=BTN_BG, cmd=None):
    btn = tk.Button(btns_frame, text=text, font=('Segoe UI', 16), fg=BTN_FG, bg=bg, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, bd=0, cursor="hand2", command=cmd)
    btn.grid(row=r, column=c, columnspan=col_span, padx=3, pady=3, sticky="nsew", ipadx=5, ipady=15)
    return btn

# Row 0 (Added delete button)
create_button("C", 0, 0, 2, BTN_HIGHLIGHT, lambda: btn_clear())
create_button("⌫", 0, 2, 1, BTN_HIGHLIGHT, lambda: btn_delete())
create_button("/", 0, 3, 1, BTN_HIGHLIGHT, lambda: btn_click("/"))

# Row 1
create_button("7", 1, 0, 1, BTN_BG, lambda: btn_click("7"))
create_button("8", 1, 1, 1, BTN_BG, lambda: btn_click("8"))
create_button("9", 1, 2, 1, BTN_BG, lambda: btn_click("9"))
create_button("*", 1, 3, 1, BTN_HIGHLIGHT, lambda: btn_click("*"))

# Row 2
create_button("4", 2, 0, 1, BTN_BG, lambda: btn_click("4"))
create_button("5", 2, 1, 1, BTN_BG, lambda: btn_click("5"))
create_button("6", 2, 2, 1, BTN_BG, lambda: btn_click("6"))
create_button("-", 2, 3, 1, BTN_HIGHLIGHT, lambda: btn_click("-"))

# Row 3
create_button("1", 3, 0, 1, BTN_BG, lambda: btn_click("1"))
create_button("2", 3, 1, 1, BTN_BG, lambda: btn_click("2"))
create_button("3", 3, 2, 1, BTN_BG, lambda: btn_click("3"))
create_button("+", 3, 3, 1, BTN_HIGHLIGHT, lambda: btn_click("+"))

# Row 4
create_button("0", 4, 0, 2, BTN_BG, lambda: btn_click("0"))
create_button(".", 4, 2, 1, BTN_BG, lambda: btn_click("."))
create_button("=", 4, 3, 1, BTN_HIGHLIGHT, lambda: btn_equal())

# Configure grid weights for uniform sizing
for i in range(5):
    btns_frame.rowconfigure(i, weight=1)
for i in range(4):
    btns_frame.columnconfigure(i, weight=1)

# --- Owner Frame ---
owner_frame = tk.Frame(window, bg="black") # Changed background to black

# Centered large text
owner_label = tk.Label(owner_frame, text="ELIAS MONCY", font=('Segoe UI', 32, 'bold'), bg="black", fg="white") # Text color is white
owner_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Back button
back_btn = tk.Button(owner_frame, text="Back to Calculator", font=('Segoe UI', 12), fg=BTN_FG, bg=BTN_HIGHLIGHT, activebackground=BTN_ACTIVE_BG, activeforeground=BTN_FG, bd=0, cursor="hand2", command=show_calc_page)
back_btn.pack(side=tk.BOTTOM, fill=tk.X, padx=15, pady=20, ipady=8)

window.mainloop()
