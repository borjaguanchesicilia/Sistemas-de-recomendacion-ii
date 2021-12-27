# Sistemas de recomendación: Modelos basados en contenidos.

### Información de uso:

* Se ha realizado una herramienta para calcular la similaridad entre pares de documentos, de manera que se obtiene una medida de similitud o de igualdad entre dichos documentos mediante la similitud coseno.


* Para procesar cada fichero, se lee cada línea (documento) y se realiza una tarea de preprocesado, para que cada documento sea idéntico y así poder trabajar de manera más eficaz:

   * Eliminación de los signos de puntuación.
   * Eliminación de espacios en blanco.
   * Eliminación de los números.
   * Transformar cada palabra a minuscúla.


* A continuación, y como paso previo a realizar el cálculo de similitud, se calculan las frecuencias con las que aparece una palabra en cada documento y en cuántos documentos aparece, el inverso logarítmico de la frecuencia del documento y se normaliza el vector de términos.


#### Ejemplo de uso:

* Nos encontramos en un directorio, donde se tiene el subdirectorio /scr con el código fuente y el subdirectorio /docs con los ejemplos de ficheros con "documentos". 

			python3.6 src/main.py docs/f1.txt
        
    * **src/main.py** Se ejecuta el programa.
    
    * **docs/f1.txt** Se indica el fichero a analizar.


### Datos sobre el código:

* Fichero ***main.py***: Contiene la invocación de las funciones de lectura de fichero, del cálculo de datos que se solicitan (**tf**, **idf**, **tf-idf**) y de la similitud. Además se comprueba que el fichero existe y se realiza el formateado de los resultados.


* Fichero ***operaciones.py***: Contiene la implementación de las funciones para la lectura del fichero de entrada, del cáculo de **tf**, **idf**, **tf-idf** y la propia función que calcula la similitud.

* Fichero ***operacionesSimilitud.py***: Contiene la implementación de las funciones necesarias para el cálculo de la similitud.