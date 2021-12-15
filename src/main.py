import sys
from operaciones import *


def inicializar():

    matricesTerminosAux = []; documentos = []

    try:
        totalDocs = int(sys.argv[1])
    except:
        print("ERROR: El primer argumento debe ser el número de documentos que quiere analizar.")
    else:

        i = 1

        while i != totalDocs+1:  

            try:
                nombreF = sys.argv[i+1]
            except:
                print("ERROR: Debe introducir el nombre del fichero como argumento.")
            else:
                try:
                    open(nombreF, 'r')
                except:
                    print(f'ERROR: El fichero {nombreF} no existe')
                else:
                    matrizTerminos = lecturaFichero(nombreF)
                    documentos.append(nombreF)
                    matricesTerminosAux.append(matrizTerminos)

            i += 1

        matricesTerminos = operacionesContenido(matricesTerminosAux, totalDocs)

        headers = ["Índice del término", "Término", "TF", "IDF", "TF-IDF"]; j = 0
        for i in matricesTerminos:
            print(f'Documento: {documentos[j]} \n')
            print(tabulate(i, headers = headers, tablefmt="fancy_grid", showindex=True), "\n\n")
            j += 1
            
if __name__ == "__main__":
    inicializar()