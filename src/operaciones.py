from tabulate import tabulate
from math import log, log10


def lecturaFichero(nombreF):

    matrizTerminos = []; documento = {}; matrizPalabras = []

    fichero = open(nombreF, 'r')
    palabra = ""; contador = 0
    linea = fichero.readline()
    

    while linea != "":
        for j in range(len(linea)):
            if  linea[j] == " ": # Si hay una espacio o un salto de línea hay una nueva palabra en "palabra"
                if (palabra != ""):
                    
                    if palabra in documento:
                        frecuencia = documento[palabra]
                        documento[palabra] = frecuencia + 1
                        documento = dict(sorted(documento.items(), key=lambda key: key[0]))

                    else:
                        documento[palabra] = 1
                        documento = dict(sorted(documento.items(), key=lambda key: key[0]))
                        if palabra not in matrizPalabras:
                            matrizPalabras.append(palabra)
                            matrizPalabras.sort()
                    palabra = ""
            elif linea[j] != "," and linea[j] != "." and linea[j].isdigit() != True: # Si el valor del substring no es una , un . o un número agregamos la substring a la palabra
                palabra +=  linea[j].lower()
            elif j == len(linea) - 1:
                break
                
        matrizTerminos.append(documento)
        linea = fichero.readline()
        palabra = ""; documento = {}; contador += 1


    fichero.close()

    i = 0
    while i <= len(matrizPalabras)-1:
        docs = 0; palabra = matrizPalabras[i]
        for j in matrizTerminos:
            if palabra in j:
                docs += 1
        
        for j in matrizTerminos:
            if palabra in j:
                frecuencia = j[palabra]
                j[palabra] = (frecuencia, docs)
        
        i += 1

    return matrizTerminos, contador


def operacionesContenido(matrizTerminos, n):

    matricesTerminos = []
    aux = 0

    for i in matrizTerminos:
        matriz = []
        for j in i:
            palabra = j
            frecuencia = i[palabra][0]; ocurrencias = i[palabra][1]
            
            tf = frecuencia
            idf = log10(n / ocurrencias)
            tf_idf = tf * idf

            matriz.append([palabra, tf, idf, tf_idf]) 

        matricesTerminos.append(matriz)
        aux += 1

    return matricesTerminos