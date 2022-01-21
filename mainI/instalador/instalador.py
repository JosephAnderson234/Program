from email import message
import urllib.request
import zipfile
import time
from colorama import init, Fore, Back, Style, Cursor

#from delete.eliminador import Eliminador



#r = urllib.request.urlopen(url)
#f = open(file, "wb")
#f.write(r.read())

#fzip = zipfile.ZipFile(file)
#fzip.extractall()

#f.close() 

init()

class Installer:
    def __init__(self, link, name):
        self.link = link
        self.name = name
        self.download()
        
    def download(self):
        message = Fore.CYAN + "Descargando el proyecto"
        for arc in [ message+".", message+"..", message+"..."]:
            time.sleep(1)
            print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.YELLOW+str(arc))    
        self.archive = urllib.request.urlopen(self.link)
        self.file = open(self.name, "wb")
        self.file.write(self.archive.read())
        self.extract()
        self.file.close()
    def extract(self):
        self.zip = zipfile.ZipFile(self.name)
        self.zip.extractall()
