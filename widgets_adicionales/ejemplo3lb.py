import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Listbox")

lista = tk.Listbox(root)
lista.insert(1, "Manzana")
lista.insert(2, "Banana")
lista.insert(3, "Naranja")
lista.pack()

root.mainloop()
