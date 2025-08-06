import tkinter as tk

root = tk.Tk()
root.title("Barra de herramientas")

toolbar = tk.Frame(root, bg="lightgray")

btn1 = tk.Button(toolbar, text="Nuevo")
btn2 = tk.Button(toolbar, text="Guardar")

btn1.pack(side="left", padx=2, pady=2)
btn2.pack(side="left", padx=2, pady=2)

toolbar.pack(side="top", fill="x")

root.mainloop()
