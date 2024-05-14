#os es una libreria parte de la biblioteca estandar de python

import os

# Ruta del directorio "/dev"
directorio_dev = "/dev"

# Obtener una lista de todos los archivos y directorios en el directorio "/dev"
contenido_dev = os.listdir(directorio_dev)

# Filtrar solo los directorios
directorios_dev = [nombre for nombre in contenido_dev if os.path.isdir(os.path.join(directorio_dev, nombre))]

# Imprimir la lista de directorios
print("Directorios dentro de /dev:")
for directorio in directorios_dev:
    print(directorio)
    