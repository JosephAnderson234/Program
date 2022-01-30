#from pyshortcuts import make_shortcut
import os

ruta = "C:\\Users\\Fam. Cose Rojas\\Desktop\\web\\Program\\Program\\product\\main.py"
ruta2 = r"C:\Users\Fam. Cose Rojas\Desktop\web\Program\Program\product\main.py"
destino = "C:\\Users\\Fam. Cose Rojas\\Desktop\\example.py"

os.symlink(ruta2, destino)

#make_shortcut(script='C:/Users/Fam. Cose Rojas/AppData/Local/Programs/Microsoft VS Code/Code.exe', name="TOOL F", desktop=True)