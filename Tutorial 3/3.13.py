import turtle

from tkinter import *
import math

def compute_square_root():
    def calculate():
        try:
            num = float(entry.get())
            result.set(round(math.sqrt(num), 2))
        except ValueError:
            result.set("Invalid input! Enter a valid number.")
    
    root = Tk()
    root.title("Square Root Calculator")
    
    Label(root, text="Enter a number:").grid(row=0, column=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)
    Button(root, text="Compute", command=calculate).grid(row=1, column=0, columnspan=2)
    Label(root, text="Result:").grid(row=2, column=0)
    result = StringVar()
    Label(root, textvariable=result).grid(row=2, column=1)
    
    root.mainloop()

compute_square_root()