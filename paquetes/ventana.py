import tkinter as tk
import time


class Ventana():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("640x420")
        self.ventana.resizable(0, 0)
        self.ventana.title("Reloj")
        self.ventana.config(background="blue")
        self.etiqueta = tk.Label(text="", font=(
            "Arial", 40), fg="blue", bg="white", pady=15, padx=15)
        self.etiqueta.place(x=200, y=150)
        self.actualizacion()
        self.ventana.mainloop()

    def actualizacion(self):
        hora = time.strftime("%H:%M:%S")
        self.etiqueta.configure(text=hora)
        self.ventana.after(1000, self.actualizacion)


if __name__ == "__main__":
    main = Ventana()
