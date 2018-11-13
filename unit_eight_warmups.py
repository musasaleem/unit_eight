import tkinter
root = tkinter.Tk()


def convert():
    f = int(Fahrenheit.get())
    c = 5/9*(f-32)
    Celsius.set(str(c))


Fahrenheit = tkinter.StringVar()
Celsius = tkinter.StringVar()
root.title("Temperature Converter")
F_label = tkinter.Label(root, text="fahrenheit")
F_label.grid(row=1, column=1)
Fentry = tkinter.Entry(root, textvariable=Fahrenheit)
Fentry.grid(row=1, column=2)
Centry = tkinter.Entry(root, textvariable=Celsius)
Centry.grid(row=2, column=2)
C_label = tkinter.Label(root, text="celsius")
C_label.grid(row=2, column=1)
Cbutton = tkinter.Button(root, text="convert", command=convert)
Cbutton.grid(row=3, column=1, columnspan=2)
root.mainloop()

