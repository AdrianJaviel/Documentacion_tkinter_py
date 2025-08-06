import tkinter as tk

root = tk.Tk()
root.title("Ejemplo Scale")

escala = tk.Scale(root, from_=0, to=100, orient="horizontal")
escala.pack()

root.mainloop()
