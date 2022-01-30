from sre_parse import State
import time
from unicodedata import name
import requests
from tkinter import *
from tkinter import filedialog, ttk
import os
import zipfile
from threading import Thread
#import ctypes, sys
url="https://github.com/JosephAnderson234/WebSiteOfChristmas/archive/refs/heads/main.zip"
file = "temporal.zip"

colorbg = "black"
colorfg= "#9ae66e"

class Installer:
    def __init__(self, link, name, directory, stado):
        self.link = link
        self.name = name
        self.state = stado
        self.directory = directory
        Thread(target=self.main).start()
        self.rute = str(self.directory+"/"+self.name)
        
    def main(self):
        """Declaramos las dependencias, se descarga el archivo"""
        os.system("cd " + self.directory)
        self.archive = requests.get(self.link)
        """Se crea el archivo zip """
        self.file = open(self.rute, "wb")
        self.file.write(self.archive.content)
        self.file.close()
        """Se descomprime este mismo"""
        self.zip = zipfile.ZipFile(file=self.rute)
        self.zip.extractall(path=self.directory)
        
        self.zip.close()
        self.acceso_directo()
    def acceso_directo(self):
        self.rute2 = str(self.directory+"/"+"WebSiteOfChristmas-main"+"/index.html")
        self.rute3 = self.rute2.replace("/", "\\")
        self.rute_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        
        #def is_admin():
        #    try:
        #        return ctypes.windll.shell32.IsUserAnAdmin()
        #    except:
        #        return False

        #if is_admin():
            # Code of your program here
        if self.state == 1:
            print(self.state)
            os.symlink(self.rute3, self.rute_desktop+"\\"+"index.html")
            os.remove(path=self.rute)
        else:
            os.remove(path=self.rute)
        #else:
            # Re-run the program with admin rights
            #ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        

class prcp(Toplevel):
    def __init__(self, master=None, direction=None, link=None, name=None, stado=None):    
        super(prcp, self).__init__(master)
        self.direction = direction
        self.link = link
        self.name = name
        self.stado = stado
        self.create_widgets()
        
    def update_barr(self):
        self.intentos = 0
        def barr():
            time.sleep(0.5)
            self.intentos += 1
            if self.intentos == 2:
                self.progreso.insert(0, "[+]Descargando...")
                Installer(self.link, self.name, self.direction, self.stado)
            if self.intentos == 3:
                self.progreso.delete(0, END)
                self.progreso.insert(0, "[+]Descomprimiendo...]")
            if self.intentos == 4:
                self.progreso.delete(0, END)
                self.progreso.insert(0, "[+]Completando instalacion...]")
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

    def execute(self):
        self.butonInstaller.config(text="aceptar", command=self.master.destroy)
        self.newTop = prcp(self.master, self.drc.get(), url, file, self.stado_of_check.get())
        self.newTop.iconbitmap("icon.ico")
        self.newTop.resizable(width=False, height=False)
        self.newTop.configure(bg=colorbg)
        self.newTop.geometry("500x300")
        self.newTop.grab_set() # Mantiene el foco de la ventana hasta que se cierre y devuelve la interacción con la ventana principal el root en este caso.
        self.newTop.focus_set() # Mantiene el foco cuando se abre la ventana.
        self.newTop.mainloop()
        

    def create_widgets(self):
        self.lbl = Label(self, text="Bienvenido al instalador de TOOL F", font=("Verdana", 20), bg=colorbg, fg=colorfg)
        self.lbl.pack(pady=10)
        self.lbld = Label(self, text="Seleccione la carpeta de destino", font=("Verdana", 10), bg=colorbg, fg=colorfg)
        self.lbld.pack(pady=10)
        self.directoryNow = os.getcwd()
        self.drc= Entry(self, width=70, bg=colorbg, fg=colorfg)
        self.drc.insert(0, self.directoryNow)
        self.drc.place(x=50, y=100)
        def qst():
            dfile = filedialog.askdirectory(parent=self, title="Seleccione la carpeta de destino")
            self.drc.delete(0, END)
            self.drc.insert(0, dfile)
        self.boton = Button(self, text="...", command=qst, bg=colorfg, fg=colorbg)
        self.boton.place(x=450, y=100, width=20, height=20)
        
        """Se establece el boton de instalar y el del acceso directo"""
        self.stado_of_check = IntVar()
        self.vrfAcc = Checkbutton(self, text="Agregar acceso directo", bg=colorbg, fg=colorfg, variable=self.stado_of_check, highlightcolor=colorbg, activebackground=colorbg, activeforeground=colorfg, selectcolor=colorbg, onvalue=1, offvalue=0)
        self.vrfAcc.place(x=50, y=150)
        self.butonInstaller = Button(self, text="siguiente", command=self.execute, bg=colorfg, fg=colorbg)
        self.butonInstaller.place(x=50, y=200)
        print(self.stado_of_check.get())
        

window = Tk()

window.geometry("500x250")
window.resizable(False, False)
window.title("Instalador")
window.iconbitmap("icon.ico")

app = Programa(window)
app.mainloop()