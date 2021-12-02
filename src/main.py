import sys
from operaciones import *

def inicializar():

    try:
        nombreF = sys.argv[1]
    except:
        print("ERROR: Debe introducir el nombre del fichero como argumento.")
    else:
        try:
            open(nombreF, 'r')
        except:
            print("ERROR: El fichero no existe")
        else:
            lecturaFichero(nombreF)
            print(matriz)


if __name__ == "__main__":
    inicializar()