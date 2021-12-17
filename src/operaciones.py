from tabulate import tabulate
from math import log, log10, sqrt


def lecturaFichero(nombreF):

    matrizTerminos = []; documento = {}; matrizPalabras = []

    fichero = open(nombreF, 'r')
    palabra = ""; contador = 0
    linea = fichero.readline()
    

    while linea != "":
        for j in range(len(linea)):
            if  linea[j] == " " or linea[j] == "\n": # Si hay una espacio o un salto de línea hay una nueva palabra en "palabra"
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


def calcularSimilitud(matrizTerminos):

    for i in matrizTerminos:
        for j in range(len(i)):
            valores = i[j]
            i[j] = [valores[0], valores[1], valores[2], valores[3], 1 + log10(valores[1])]

    longitudVector = []

    for i in matrizTerminos:
        sumatorio = 0
        for j in range(len(i)):
            sumatorio += pow(i[j][4], 2)

        longitudVector.append(sqrt(sumatorio))


    k = 0
    for i in matrizTerminos:
        longitud = longitudVector[k];
        for j in range(len(i)):
            valores = i[j]
            normalizacion = (valores[4] / longitud)
            i[j] = [valores[0], valores[1], valores[2], valores[3], valores[4], normalizacion]
        k += 1


    # Similaridad
    k = 0
    similaridad = []
    for i in range(len(matrizTerminos)):
        documento1 = matrizTerminos[i]
        for j in range(len(matrizTerminos)):
            if i != j: # Calculamos la similaridad entre todos los pares de documentos
                documento2 = matrizTerminos[j]; sim = 0
                for k in range(len(documento1)):
                    for l in range(len(documento2)):
                        if documento1[k][0] == documento2[l][0]:
                            valor1 = documento1[k][5]; valor2 = documento2[l][5]
                            sim += (valor1 * valor2)
                similaridad.append((i+1, j+1, sim))


    for i in range(len(similaridad)):
        print(f"cos({similaridad[i][0]}, {similaridad[i][1]}) = {similaridad[i][2]}")