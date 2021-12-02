matriz = []

def lecturaFichero(nombreF):

    global matriz

    fichero = open(nombreF, 'r')
    letras = ""; palabra = []
    linea = fichero.readline()
    
    while linea != "":
        for j in range(len(linea)):
            if  linea[j] == " " or linea[j] == "\n": # Si hay una espacio o un salto de línea hay una nueva palabra en "letras"
                if (letras != ""):
                    palabra.append(letras); letras = ""
            elif linea[j] != "," and linea[j] != "." and linea[j].isdigit() != True:
                letras +=  linea[j].lower()
            elif j == len(linea) - 1:
                if (letras != ""): # Si se ha llegado al final del readline hay una nueva palabra en "letras"
                    palabra.append(letras); letras = ""
            
        matriz.append(palabra); palabra = []
        linea = fichero.readline()

    fichero.close()