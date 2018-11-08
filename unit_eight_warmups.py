import tkinter
root = tkinter.Tk()
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

root.mainloop()

