import os

class Eliminador:
    def __init__(self, nm):
        self.nm = nm
        self.eliminar()
    def eliminar(self):
        os.remove(self.nm)
