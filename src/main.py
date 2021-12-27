import sys
from operaciones import *


def inicializar():

    matricesTerminosAux = []; ficheros = []

    try:
        nombreF = sys.argv[1]
    except:
        print("ERROR: Debe introducir el nombre del fichero como argumento.")
    else:
        try:
            open(nombreF, 'r')
        except:
            print(f'ERROR: El fichero {nombreF} no existe.')
        else:
            matrizTerminos, n = lecturaFichero(nombreF)
            matrizTerminos = operacionesContenido(matrizTerminos, n)

            headers = ["Índice del término", "Término", "TF", "IDF", "TF-IDF"]; j = 1
            for i in matrizTerminos:
                print(f'Documento: {j} \n')
                print(tabulate(i, headers = headers, tablefmt="fancy_grid", showindex=True), "\n\n")
                j += 1

            similaridad(matrizTerminos)
            
if __name__ == "__main__":
    inicializar()