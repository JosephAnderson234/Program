from instalador.instalador import Installer
from delete.eliminador import Eliminador

url="https://github.com/Programadoresdel3D/Program/archive/refs/heads/main.zip"
file = "temporal.zip"

Installer(url, file)
Eliminador(file)