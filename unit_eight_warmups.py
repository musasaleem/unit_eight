import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")
F_label = tkinter.Label(root, text="Fahrenheit")
F_label.grid(row=1, column=1)
Fentry = tkinter.Entry(root)
Fentry.grid(row=1, column=2)
Centry = tkinter.Entry(root)
Centry.grid(row=2, column=2)
C_label = tkinter.Label(root, text="Celsius")
C_label.grid(row=2, column=1)

root.mainloop()

