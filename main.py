import tkinter as tk
from tkinter import ttk
import math


def on_click(character):
    """Handles button clicks, updating the display."""
    current_text = display.get()
    if current_text == "Error":
        display.set(character)
    else:
        display.set(current_text + character)


def evaluate():
    """Evaluates the expression in the display and shows the result."""
    try:
        # Handle scientific functions manually
        expression = display.get()
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('exp', 'math.exp')
        expression = expression.replace('log', 'math.log')
        expression = expression.replace('sqrt', 'math.sqrt')
        expression = expression.replace('^', '**')
        result = eval(expression)
        display.set(result)
    except Exception:
        display.set("Error")


def clear_display():
    """Clears the display."""
    display.set("")


# Create the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Adjust window size
root.geometry("400x600")
root.resizable(False, False)

# StringVar to hold the display's content
display = tk.StringVar()

# Create the display area
display_entry = ttk.Entry(root, textvariable=display, font=("Arial", 16), justify="right")
display_entry.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# Define button labels in a layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3), ('exp', 4, 4),
    ('log', 5, 0), ('sqrt', 5, 1), ('^', 5, 2),  # Additional scientific functions
]

# Create and place buttons in the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = ttk.Button(root, text=text, command=evaluate)
    elif text == 'C':
        btn = ttk.Button(root, text=text, command=clear_display)
    else:
        btn = ttk.Button(root, text=text, command=lambda t=text: on_click(t))
    btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Adjust grid configuration
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Start the Tkinter event loop
root.mainloop()
