from instalador.instalador import Installer
from delete.eliminador import Eliminador
from tkinter import *
from tkinter import filedialog, ttk
import os

url="https://github.com/JosephAnderson234/WebSiteOfChristmas/archive/refs/heads/main.zip"
file = "temporal.zip"

colorbg = "black"
colorfg= "#9ae66e"

window = Tk()

window.geometry("500x600")
window.resizable(False, False)
window.title("Instalador")
window.iconbitmap("icon.ico")
window.config(bg=colorbg)

lbl = Label(window, text="Bienvenido al instalador de TOOL F", font=("Verdana", 20), bg=colorbg, fg=colorfg)
lbl.pack(pady=10)

lbld = Label(window, text="Seleccione la carpeta de destino", font=("Verdana", 10), bg=colorbg, fg=colorfg)
lbld.pack(pady=10)

directoryNow = os.getcwd()

drc= Entry(window, width=70, bg=colorbg, fg=colorfg)
drc.insert(0, directoryNow)
drc.place(x=50, y=100)

def qst():
    dfile = filedialog.askdirectory(parent=window, title="Seleccione la carpeta de destino")
    drc.delete(0, END)
    drc.insert(0, dfile)

boton = Button(window, text="...", command=qst, bg=colorfg, fg=colorbg)
boton.place(x=450, y=100)

def execute():
    os.system("cd " + drc.get())
    Installer(url, file)
    Eliminador(file) 

installer = Button(window, text="Instalar", command=execute, bg=colorfg, fg=colorbg)
installer.place(x=50, y=150)
window.mainloop()

