import turtle

from tkinter import *

def computer_guess_number():
    low, high = 1, 100
    attempts = 0
    
    def make_guess():
        nonlocal low, high, attempts, guess
        attempts += 1
        guess = (low + high) // 2
        label_guess.config(text=f"Is your number {guess}?")
    
    def too_small():
        nonlocal low
        low = guess + 1
        make_guess()
    
    def too_large():
        nonlocal high
        high = guess - 1
        make_guess()
    
    def correct():
        label_guess.config(text=f"Correct! Guessed in {attempts} tries.")
        button_small.config(state=DISABLED)
        button_large.config(state=DISABLED)
        button_correct.config(state=DISABLED)
    
    root = Tk()
    root.title("Computer Guesses the Number")
    
    label_guess = Label(root, text="Think of a number between 1 and 100.")
    label_guess.pack()
    
    button_small = Button(root, text="Too Small", command=too_small)
    button_small.pack()
    button_large = Button(root, text="Too Large", command=too_large)
    button_large.pack()
    button_correct = Button(root, text="Correct", command=correct)
    button_correct.pack()
    
    make_guess()
    
    root.mainloop()

computer_guess_number()