from hashlib import new
from operator import iconcat
import time
from urllib import request
import requests
from tkinter import *
from tkinter import filedialog, ttk
import os
import zipfile
from threading import Thread
from tracemalloc import start
from concurrent.futures import process

url="https://github.com/JosephAnderson234/WebSiteOfChristmas/archive/refs/heads/main.zip"
file = "temporal.zip"

colorbg = "black"
colorfg= "#9ae66e"

class Installer:
    def __init__(self, link, name, directory):
        self.link = link
        self.name = name
        self.directory = directory
        self.download()
        
    def download(self):
        os.system("cd " + self.directory)
        self.rute = str(self.directory+"/"+self.name)
        self.archive = requests.get(self.link)
        with open(self.rute, "wb") as file:
            file.write(self.archive.content)
        self.extract()
        
    def extract(self):
        self.zip = zipfile.ZipFile(file=self.rute)
        self.zip.extractall(path=self.directory)

class Eliminador:
    def __init__(self, nm, directory):
        self.nm = nm
        self.directory = directory
        self.eliminar()
    def eliminar(self):
        os.system("cd " + self.directory)
        self.rute = str(self.directory+"/"+self.nm)
        os.remove(path=self.directory+"/"+self.nm)
        

class prcp(Toplevel):
    def __init__(self, master=None, direction=None, link=None, name=None):    
        super(prcp, self).__init__(master)
        self.direction = direction
        self.link = link
        self.name = name
        self.create_widgets()
        
    def update_barr(self):
        self.intentos = 0
        def barr():
            time.sleep(0.5)
            self.intentos += 1
            if self.intentos == 2:
                self.progreso.insert(0, "[+]Descargando...")
                Installer(self.link, self.name, self.direction)
            if self.intentos == 3:
                self.progreso.delete(0, END)
                self.progreso.insert(0, "[+]Descomprimiendo...]")
            if self.intentos == 4:
                self.progreso.delete(0, END)
                self.progreso.insert(0, "[+]Completando instalacion...]")
                Eliminador(self.name, self.direction)
            if self.intentos == 10:
                self.progreso.delete(0, END)
                self.progreso.insert(0, "[+]Instalacion completada")
                self.boton.config(text="Aceptar", command=self.destroy)
            self.prg["value"] += 5
            self.update_idletasks()
            self.after(100, barr)
        barr()
    
    
    def create_widgets(self):
        self.prg = ttk.Progressbar(self, orient="horizontal", length=300)
        self.prg.pack(pady=10)
        
        self.progreso = Entry(self, bg="black", fg="#9ae66e")
        self.progreso.place(x=100, y=100, width=300, height=20)
        
        self.boton = Button(self, text="Instalar", command=self.update_barr, bg="#9ae66e", fg="black")
        self.boton.place(x=225, y=150)

class Programa(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=500, height=600, bg=colorbg)
        self.master = master
        self.pack( fill=BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        lbl = Label(self, text="Bienvenido al instalador de TOOL F", font=("Verdana", 20), bg=colorbg, fg=colorfg)
        lbl.pack(pady=10)

        lbld = Label(self, text="Seleccione la carpeta de destino", font=("Verdana", 10), bg=colorbg, fg=colorfg)
        lbld.pack(pady=10)

        directoryNow = os.getcwd()

        drc= Entry(self, width=70, bg=colorbg, fg=colorfg)
        drc.insert(0, directoryNow)
        drc.place(x=50, y=100)

        def qst():
            dfile = filedialog.askdirectory(parent=self, title="Seleccione la carpeta de destino")
            drc.delete(0, END)
            drc.insert(0, dfile)

        boton = Button(self, text="...", command=qst, bg=colorfg, fg=colorbg)
        boton.place(x=450, y=100, width=20, height=20)

        def execute():
            newTop = prcp(self.master, drc.get(), url, file)
            newTop.iconbitmap("icon.ico")
            newTop.resizable(width=False, height=False)
            newTop.configure(bg=colorbg)
            newTop.geometry("500x300")
            newTop.grab_set() # Mantiene el foco de la ventana hasta que se cierre y devuelve la interacción con la ventana principal el root en este caso.
            newTop.focus_set() # Mantiene el foco cuando se abre la ventana.
            newTop.mainloop()
            
        installer = Button(self, text="siguiente", command=execute, bg=colorfg, fg=colorbg)
        installer.place(x=50, y=150)
        

window = Tk()

window.geometry("500x200")
window.resizable(False, False)
window.title("Instalador")
window.iconbitmap("icon.ico")

app = Programa(window)
app.mainloop()