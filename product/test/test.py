from colorama import init, Fore, Back, Style, Cursor
import time

msg = "Comprobando si existe la carpeta"
print(Fore.CYAN + "========================================================================================")
for arc in ["[\] " + msg,"[|] " + msg,"[/] " + msg,"[-] " + msg]:
    time.sleep(1)
    print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.YELLOW+str(arc))
    
