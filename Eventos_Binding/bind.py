import tkinter as tk

def saludar(event):
    etiqueta.config(text="¡Hola!")

root = tk.Tk()
root.title("Ejemplo bind()")

etiqueta = tk.Label(root, text="Haz clic aquí", font=("Arial", 14))
etiqueta.pack(pady=20)

etiqueta.bind("<Button-1>", saludar)

root.mainloop()
