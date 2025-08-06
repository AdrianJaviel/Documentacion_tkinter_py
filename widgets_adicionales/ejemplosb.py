import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Spinbox")

spin = tk.Spinbox(root, from_=1, to=10)
spin.pack()

root.mainloop()
