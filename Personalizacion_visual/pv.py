import tkinter as tk

root = tk.Tk()
root.title("Personalización Visual")
root.geometry("300x200")
root.configure(bg="#222831")

etiqueta = tk.Label(root, text="Interfaz Personalizada",
                    font=("Comic Sans MS", 14, "bold"),
                    fg="white", bg="#222831")
etiqueta.pack(pady=20)

boton = tk.Button(root, text="Aceptar", bg="#00ADB5", fg="white",
                  font=("Arial", 12, "bold"))
boton.pack()

root.mainloop()
