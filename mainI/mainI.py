from instalador.instalador import Installer
from delete.eliminador import Eliminador

url="https://github.com/JosephAnderson234/Program/archive/refs/heads/main.zip"
file = "temporal.zip"

Installer(url, file)
Eliminador(file)