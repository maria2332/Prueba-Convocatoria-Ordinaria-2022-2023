"""
El cifrado Rail Fence (también llamado cifrado en zigzag) es una forma de cifrado por transposición. Funciona escribiendo su mensaje en líneas alternas a lo largo de la página y luego leyendo cada línea por turno. Veamos el desglose paso a paso para cifrar un texto usando Rail Fence Cipher:

Para encriptar un mensaje usando Rail Fence Cipher, primero necesitamos tener una clave (lo mismo para encriptar y desencriptar), que es el número de filas que tendrá para este cifrado.
Luego comenzamos a escribir las letras del texto sin formato dado en diagonal hacia el lado derecho hasta alcanzar el número de filas especificado por la clave.
Luego rebotamos hacia arriba de manera similar en diagonal hasta que llegamos a la primera fila nuevamente. Así, los alfabetos del texto plano se escriben en zig-zag.
Este ciclo continúa hasta que se alcanza el final del texto sin formato. Luego se leen las filas individuales para obtener el texto cifrado.
Considerar un ejemplo nos aclararía las cosas. Tomemos un ejemplo donde: El texto sin formato se da como " defend the east wall " y el número de rieles (clave) = 3, luego el proceso de encriptación es como se muestra a continuación:
El cifrado Rail Fence con una clave de 3

Tenga en cuenta que al final del mensaje hemos insertado dos letras "X", que se llaman nulos y actúan como marcadores de posición. Esto se hace para asegurarse de que el mensaje encaje perfectamente en la cuadrícula, de modo que haya el mismo número de letras en la fila superior y en la fila inferior.

Ahora, leer la imagen fila por fila nos da el texto cifrado como "DNETLEEDHESWLXFTAAX".

Para descifrar un texto cifrado codificado con Rail Fence Cipher, tenemos que reconstruir la cuadrícula diagonal utilizada para cifrar el mensaje. Comenzamos escribiendo el mensaje, pero dejando una estrella en lugar de los espacios por ocupar (como se muestra en la siguiente figura). Gradualmente, puede reemplazar todas las estrellas con las letras correspondientes y leer el texto sin formato de la tabla de manera similar al cifrado

Colocación de estrellas en el lugar de los espacios a ocupar

Veamos el desglose por pasos:

Comenzamos haciendo una cuadrícula (matriz de rieles) con tantas filas como la clave dada (número de rieles) y tantas columnas como la longitud del texto cifrado.
Luego colocamos la primera letra en el cuadrado superior izquierdo y avanzamos en diagonal hacia abajo donde están presentes las letras.
Cuando volvemos a la fila superior, colocamos la siguiente letra en el texto cifrado. Continuamos este proceso a lo largo de la fila y comenzamos la siguiente fila cuando lleguemos al final.
Atravesamos la matriz en forma de zig-zag para obtener el texto plano original.
 Escriba una función/método que tome 2 argumentos, una cadena y el número de rieles, y devuelva la cadena CODIFICADA.

Escriba una segunda función/método que tome 2 argumentos, una cadena codificada y el número de rieles, y devuelva la cadena DECODIFICADA.

Tanto para la codificación como para la decodificación, asuma un número de rieles >= 2 y que pasar una cadena vacía devolverá una cadena vacía.

Tenga en cuenta que el ejemplo anterior excluye la puntuación y los espacios solo por simplicidad. Sin embargo, hay pruebas que incluyen puntuación. No filtre la puntuación, ya que son parte de la cadena.
"""

import ast as main 
#calcular cuantas filas tiene la matriz de cifrado 
def calcular_filas(texto, clave):
    if len(texto) < clave:
        return len(texto)
    else:
        return clave

#calcular cuantas columnas tiene la matriz de cifrado
def calcular_columnas(texto, clave):
    if len(texto) < clave:
        return clave
    else:
        return len(texto)

#calcular el tamaño de la matriz de cifrado
def calcular_tamano_matriz(texto, clave):
    return calcular_filas(texto, clave) * calcular_columnas(texto, clave)

import numpy as np

#crear la matriz de cifrado
def crear_matriz(texto, clave):
    matriz = np.zeros((calcular_filas(texto, clave), calcular_columnas(texto, clave)))
    return matriz

#llenar la matriz de cifrado
def llenar_matriz(matriz, texto, clave):
    for i in range(len(texto)):
        matriz[i % clave][i] = texto[i]
    return matriz

#obtener el texto cifrado
def obtener_texto_cifrado(matriz, texto, clave):
    texto_cifrado = ""
    for i in range(clave):
        for j in range(len(texto)):
            if matriz[i][j] != 0:
                texto_cifrado += matriz[i][j]
    return texto_cifrado

#codificar el texto
def codificar(texto, clave):
    if len(texto) == 0:
        return ""
    else:
        matriz = crear_matriz(texto, clave)
        matriz = llenar_matriz(matriz, texto, clave)
        texto_cifrado = obtener_texto_cifrado(matriz, texto, clave)
        return texto_cifrado

#obtener el texto sin formato
def obtener_texto_sin_formato(matriz, texto, clave):
    texto_sin_formato = ""
    for i in range(len(texto)):
        texto_sin_formato += matriz[i % clave][i]
    return texto_sin_formato

#decodificar el texto
def decodificar(texto, clave):
    if len(texto) == 0:
        return ""
    else:
        matriz = crear_matriz(texto, clave)
        matriz = llenar_matriz(matriz, texto, clave)
        texto_sin_formato = obtener_texto_sin_formato(matriz, texto, clave)
        return texto_sin_formato

if __name__ == "__main__":
    main()





