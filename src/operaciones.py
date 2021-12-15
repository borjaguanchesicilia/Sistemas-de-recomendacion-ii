from tabulate import tabulate
from math import log, log10

def lecturaFichero(nombreF):

    matrizTerminos = {}

    fichero = open(nombreF, 'r')
    letras = ""
    linea = fichero.readline()
    
    while linea != "":
        for j in range(len(linea)):
            if  linea[j] == " " or j == len(linea) - 1: # Si hay una espacio o un salto de línea hay una nueva palabra en "letras"
                if (letras != ""):
                    if letras in matrizTerminos:
                        frecuencia = matrizTerminos[letras]
                        matrizTerminos[letras] = frecuencia + 1
                        matrizTerminos = dict(sorted(matrizTerminos.items(), key=lambda key: key[0]))
                    else:
                        matrizTerminos[letras] = 1
                    letras = ""
            elif linea[j] != "," and linea[j] != "." and linea[j].isdigit() != True:
                letras +=  linea[j].lower()
            
        linea = fichero.readline()

    fichero.close()

    return matrizTerminos


def operacionesContenido(matrices, n):

    matricesTerminos = []

    for i in matrices:
        matriz = []
        for j in i:
            palabra = j
            frecuencia = i[palabra]

            k = 0; ocurrencias = 0
            while k < len(matrices):
                if palabra in matrices[k]:
                    ocurrencias += 1
                k += 1
            
            tf = frecuencia
            idf = log10(n / ocurrencias)
            tf_idf = tf * idf
            print(n, ocurrencias, idf, tf_idf)

            matriz.append([palabra, tf, idf, tf_idf]) 

        matricesTerminos.append(matriz)

    return matricesTerminos