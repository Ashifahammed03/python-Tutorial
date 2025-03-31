import turtle

def convert_temp():
    from tkinter import *
    def f_to_c():
        celsius_var.set(round((float(fahrenheit_var.get()) - 32) * 5 / 9, 2))
    def c_to_f():
        fahrenheit_var.set(round(float(celsius_var.get()) * 9 / 5 + 32, 2))
    
    root = Tk()
    root.title("Temperature Converter")
    
    fahrenheit_var = StringVar(value="32")
    celsius_var = StringVar(value="0.0")
    
    Label(root, text="Fahrenheit").grid(row=0, column=0)
    Label(root, text="Celsius").grid(row=0, column=1)
    
    Entry(root, textvariable=fahrenheit_var).grid(row=1, column=0)
    Entry(root, textvariable=celsius_var).grid(row=1, column=1)
    
    Button(root, text=">>>>", command=f_to_c).grid(row=2, column=0)
    Button(root, text="<<<<", command=c_to_f).grid(row=2, column=1)
    
    root.mainloop()