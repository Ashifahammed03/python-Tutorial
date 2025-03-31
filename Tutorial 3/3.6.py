import turtle

from tkinter import *

def convert_to_uppercase():
    def convert():
        output_var.set(input_var.get().upper())
    
    root = Tk()
    root.title("Uppercase Converter")
    
    input_var = StringVar()
    output_var = StringVar()
    
    Label(root, text="Enter text:").grid(row=0, column=0)
    Entry(root, textvariable=input_var).grid(row=0, column=1)
    Button(root, text="Convert", command=convert).grid(row=1, column=0, columnspan=2)
    Label(root, text="Uppercase:").grid(row=2, column=0)
    Label(root, textvariable=output_var).grid(row=2, column=1)
    
    root.mainloop()

convert_to_uppercase()
