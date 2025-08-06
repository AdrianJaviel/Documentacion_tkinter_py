import tkinter as tk

def opcion1():
    print("Seleccionaste opción 1")

root = tk.Tk()
root.title("Ejemplo de menú")

barra_menu = tk.Menu(root)
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Opción 1", command=opcion1)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

root.mainloop()
