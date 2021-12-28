from math import log10, sqrt


def calcularTf(matrizTerminos):

    for i in matrizTerminos:
        for j in range(len(i)):
            valores = i[j]
            i[j] = [valores[0], valores[1], valores[2], valores[3], 1 + log10(valores[1])]

    return matrizTerminos


def calcularLongitud(matrizTerminos):

    longitudVector = []

    for i in matrizTerminos:
        sumatorio = 0
        for j in range(len(i)):
            sumatorio += pow(i[j][4], 2)

        longitudVector.append(sqrt(sumatorio))

    return longitudVector


def calcularNormalizacion(longitudVector, matrizTerminos):
    
    k = 0
    for i in matrizTerminos:
        longitud = longitudVector[k];
        for j in range(len(i)):
            valores = i[j]
            normalizacion = (valores[1] / longitud)
            i[j] = [valores[0], valores[1], valores[2], valores[3], valores[4], normalizacion]
        k += 1

    return matrizTerminos


def calcularSimilaridad(matrizTerminos):

    k = 0; similaridad = []

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

    return similaridad