import os
import time
from colorama import init, Fore, Back, Style, Cursor

init()

class app:
    def __init__(self):
        self.main()
        self.rute()
            
    def main(self):
        os.system("color a")
        print("\n \n \n \n")

        print(Fore.CYAN + "========================================================================================")
        print(Fore.CYAN + "!Bienvenido a su asistente de Firebase:")
        print("***************************************************")
        print("    =======  /=====\  /=====\  ||     ======")
        print("      ||     ||   ||  ||   ||  ||     ||")
        print("      ||     ||   ||  ||   ||  ||     ====")
        print("      ||     ||   ||  ||   ||  ||     ||")
        print("      ||     \=====/  \=====/  =====  ||")
        print("***************************************************")
        
        print("")
        print("")
        time.sleep(2)
        init(autoreset=True)
        print(Fore.YELLOW + "========================================================================================")
        print(Fore.YELLOW + "Recuerde que nesecita node.js instaalado") 
        print("")
        print("")
        print("")
        print("")
        time.sleep(2)
    
    def test(self, drc):
        msg = "Comprobando si existe la carpeta del proyecto"
        for arc in ["[\] " + msg,"[|] " + msg,"[/] " + msg,"[-] " + msg]:
            time.sleep(1)
            print(Cursor.UP(1)+Cursor.FORWARD(20)+Fore.YELLOW+str(arc))
        time.sleep(2)
        if os.path.isdir(drc):
            init(autoreset=True)
            print("")
            print(Fore.GREEN + "[+] Dirrecion comprobada")
            print("")
            time.sleep(2)
            self.seleccionardor(True)
        else:
            init(autoreset=True)
            print(Fore.RED + "[-] Lo sentimos la direccion correspondiente no es válida")
            time.sleep(2)
            self.seleccionardor(False)
    
    def rute(self):
        init(autoreset=True)
        print(Fore.CYAN + "Okey? Comenzemos, pasame la dirección del proyexto aqui:")
        self.direction = str(input(Fore.CYAN + "--->:"))
        self.test(self.direction)
            
    def seleccionardor(self, rqst):
        if rqst == True:
            init(autoreset=True)
            os.system("cd " + self.direction)
            print(Fore.CYAN + "Elija nuestras opciones:")
            print(Fore.CYAN + "Ubicación actual: " + self.direction)
            print(Fore.CYAN + "! Reacuerde si va a subir un nuevo proyecto ejecute codigo por codigo")
            print("")
            print("1-Instalar firebase")
            print("")
            print("2-Login firebase")
            print("")
            print("3-Init firebase")
            print("")
            print("4- Deploy firebase")
            print("")
            print("5-Actualizar archivos en firebase")
            print("")
            print("6-Cambiar de dirección")
            try: 
                answer = int(input(Fore.CYAN + "--->:"))
            except ValueError:
                print("")
                print("")
                print(Fore.RED + "[-]Ups algo salio mal asegurate de que tu repuesta sea un numero dentro de las lista de opciones")
                print("")
                time.sleep(6)
                self.seleccionardor()
            if answer == 1:
                print(Fore.GREEN + "[+] Ejecutando código")
                print(Fore.GREEN + "[+] Espere...")
                time.sleep(1)
                os.system("npm install -g firebase-tools")
                print("")
                print(Fore.GREEN + "[+] EL código y la función fueron ejecutados con éxito")
                time.sleep(1)
                print("¿Quieres ir al menu?  y/n")
                reintento = str(input("       :"))
                if reintento == "y" or reintento ==" Y":
                    self.seleccionardor()
                elif reintento == "n" or reintento == "N":
                    print("Hasta pronto :D")
                    time.sleep(1)
            if answer == 2:
                print(Fore.GREEN + "[+] Ejecutando código")
                print(Fore.GREEN + "[+] Espere...")
                time.sleep(1)
                os.system("firebase login")
                print("")
                print(Fore.GREEN + "[+] EL código y la función fueron ejecutados con éxito")
                time.sleep(1)
                print("¿Quieres ir al menu?  y/n")
                reintento = str(input("       :"))
                if reintento == "y" or reintento ==" Y":
                    self.seleccionardor()
                elif reintento == "n" or reintento == "N":
                    print("Hasta pronto")
                    time.sleep(1)
            if answer == 3:
                print(Fore.GREEN + "[+] Ejecutando código")
                print(Fore.GREEN + "[+] Espere...")
                time.sleep(1)
                os.system("firebase init")
                print("")
                print(Fore.GREEN + "[+] EL código y la función fueron ejecutados con éxito")
                time.sleep(1)
                print("¿Quieres ir al menu?  y/n")
                reintento = str(input("       :"))
                if reintento == "y" or reintento ==" Y":
                    self.seleccionardor()
                elif reintento == "n" or reintento == "N":
                    print("Hasta pronto")
                    time.sleep(1)
            if answer == 4:
                print(Fore.GREEN + "[+] Ejecutando código")
                print(Fore.GREEN + "[+] Espere...")
                time.sleep(1)
                os.system("firebase deploy")
                print("")
                print(Fore.GREEN + "[+] EL código y la función fueron ejecutados con éxito")
                time.sleep(1)
                print("¿Quieres ir al menu?  y/n")
                reintento = str(input("       :"))
                if reintento == "y" or reintento ==" Y":
                    self.seleccionardor()
                elif reintento == "n" or reintento == "N":
                    print("Hasta pronto")
                    time.sleep(1)
            if answer == 5:
                print(Fore.GREEN + "[+] Ejecutando código")
                print(Fore.GREEN + "[+] Espere...")
                time.sleep(1)
                print("")
                os.system("firebase deploy --only hosting")
                #os.system("")
                print("")
                print(Fore.GREEN + "[+] EL código y la función fueron ejecutados con éxito")
                print("¿Quieres ir al menu?  y/n")
                reintento = str(input("       :"))
                if reintento == "y" or reintento ==" Y":
                    self.seleccionardor()
                elif reintento == "n" or reintento == "N":
                    print("Hasta pronto")
                    time.sleep(1)
            if answer == 6:
                print(Fore.CYAN + "[+] Inserte su dirección")
                time.sleep(2)
                self.rute()
            else:
                print("")
                print("")
                print(Fore.RED + "[-]Ups algo salio mal asegurate de que tu repuesta sea un numero dentro de las lista de opciones")
                print("")
                time.sleep(6)
                self.seleccionardor()
        else:
            time.sleep(2)
            print("")
            print("[-] Vuelve a intentarlo")
            self.rute()
app()