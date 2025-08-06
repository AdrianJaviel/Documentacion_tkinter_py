import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Checkbutton")

var = tk.IntVar()
check = tk.Checkbutton(root, text="Acepto los términos", variable=var)
check.pack()


