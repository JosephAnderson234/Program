from tkinter import *

import tkinter
    
top = Tk()
CheckVar1 = BooleanVar()
CheckVar2 = BooleanVar()
C1 = Checkbutton(top, text = "Music", variable = CheckVar1, onvalue = True, offvalue = False, height=5, width = 20, )
C2 = Checkbutton(top, text = "Video", variable = CheckVar2, onvalue = True, offvalue = False, height=5, width = 20)
C1.pack()
C2.pack()

def tverificar():
    print(CheckVar1.get())
    print(CheckVar2.get())

boton = Button(top, text = "Verificar", command = tverificar)
boton.pack()
top.mainloop()