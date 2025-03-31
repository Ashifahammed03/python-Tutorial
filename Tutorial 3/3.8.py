import turtle

from tkinter import *
from tkinter import messagebox
import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    
    def check_guess():
        nonlocal attempts
        try:
            guess = int(entry.get())
            attempts += 1
            if guess > number:
                label_result.config(text="Too large, try again!")
            elif guess < number:
                label_result.config(text="Too small, try again!")
            else:
                label_result.config(text=f"Correct! You guessed in {attempts} tries.")
                entry.config(state=DISABLED)
                button_guess.config(state=DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number.")
    
    root = Tk()
    root.title("Guess the Number")
    
    Label(root, text="Enter a number between 1 and 100:").grid(row=0, column=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)
    button_guess = Button(root, text="Guess", command=check_guess)
    button_guess.grid(row=1, column=0, columnspan=2)
    label_result = Label(root, text="")
    label_result.grid(row=2, column=0, columnspan=2)
    
    root.mainloop()

guess_the_number()
