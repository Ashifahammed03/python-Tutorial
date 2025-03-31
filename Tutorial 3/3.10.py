import turtle

from tkinter import *

def calculate_bounce_distance():
    try:
        height = float(entry_height.get())
        index = float(entry_index.get())
        bounces = int(entry_bounces.get())
        
        total_distance = height
        current_height = height * index
        
        for _ in range(bounces - 1):
            total_distance += 2 * current_height
            current_height *= index
        
        result_var.set(f"Total Distance: {round(total_distance, 2)}")
    except ValueError:
        result_var.set("Invalid input! Enter valid numbers.")

root = Tk()
root.title("Bouncy Ball Distance Calculator")

Label(root, text="Initial Height:").grid(row=0, column=0)
entry_height = Entry(root)
entry_height.grid(row=0, column=1)

Label(root, text="Bounciness Index:").grid(row=1, column=0)
entry_index = Entry(root)
entry_index.grid(row=1, column=1)

Label(root, text="Number of Bounces:").grid(row=2, column=0)
entry_bounces = Entry(root)
entry_bounces.grid(row=2, column=1)

Button(root, text="Calculate", command=calculate_bounce_distance).grid(row=3, column=0, columnspan=2)

result_var = StringVar()
Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=2)

root.mainloop()
