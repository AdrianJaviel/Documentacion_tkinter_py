import tkinter as tk

root = tk.Tk()
root.title("Ejemplo place()")
root.geometry("300x200")

tk.Label(root, text="Nombre:").place(x=30, y=50)
tk.Entry(root).place(x=100, y=50)

tk.Button(root, text="Guardar").place(x=120, y=100)

root.mainloop()
