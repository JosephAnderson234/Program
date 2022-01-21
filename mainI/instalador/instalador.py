import urllib.request
import zipfile
import os

#from delete.eliminador import Eliminador



#r = urllib.request.urlopen(url)
#f = open(file, "wb")
#f.write(r.read())

#fzip = zipfile.ZipFile(file)
#fzip.extractall()

#f.close() 

class Installer:
    def __init__(self, link, name):
        self.link = link
        self.name = name
        self.download()
        
    def download(self):
        self.archive = urllib.request.urlopen(self.link)
        self.file = open(self.name, "wb")
        self.file.write(self.archive.read())
        self.extract()
        self.file.close()
    def extract(self):
        self.zip = zipfile.ZipFile(self.name)
        self.zip.extractall()
