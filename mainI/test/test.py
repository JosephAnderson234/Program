import tkinter as tk
import random
def actualizar_etiqueta():
    numero_aleatorio = random.randint(1, 100)
    etiqueta1.config(text=f"Número aleatorio: {numero_aleatorio}")
    # Volver a programar esta función para dentro de dos segundos.
    ventana.after(2000, actualizar_etiqueta)
ventana = tk.Tk()
ventana.title("Ejemplo after() en Tk")
ventana.config(width=400, height=300)
etiqueta1 = tk.Label(text="¡Hola mundo!")
etiqueta1.place(x=100, y=70)
ventana.after(2000, actualizar_etiqueta)
ventana.mainloop()