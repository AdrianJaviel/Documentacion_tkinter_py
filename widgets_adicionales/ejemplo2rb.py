import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Radiobutton")

opcion = tk.StringVar()

tk.Radiobutton(root, text="Opción A", variable=opcion, value="A").pack()
tk.Radiobutton(root, text="Opción B", variable=opcion, value="B").pack()

root.mainloop()
