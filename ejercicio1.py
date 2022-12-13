"""
Ejercicio 1

El trabajo que realizaremos consiste en la elaboración de un modelo para resolver sudokus, para ello, crea una función que resuelva un Sudoku de 9x9.
Un sudoku es un puzzle matemático que se construye sobre una rejilla de 9x9 casillas. El objetivo es rellenarla con números enteros del 1 al 9 según las siguientes restricciones:
No se pueden repetir números en una misma fila.
No se pueden repetir números en una misma columna.
No se pueden repetir números en una misma subcuadrícula de 3x3 de las 9 que componen la rejilla.
Esta función recibe un argumento que consiste en una matriz de 2D. Un valor de 0 representa un cuadrado desconocido.
El sudoku a resolver ha de estar bien planteado, i.e., ha de tener solución única. Esto se cumple si se parte de unas condiciones iniciales adecuadas, que consisten en números ya fijados en algunas de las casillas del sudoku. Un sudoku bien planteado sin resolver podría ser, e.g., el mostrado en la siguiente figura:

"""

from ast import main

def repetido_fila(sudoku, fila, numero):
    for i in range(9):
        if sudoku[fila][i] == numero:
            return True
    return False

def repetido_columna(sudoku, columna, numero):
    for i in range(9):
        if sudoku[i][columna] == numero:
            return True
    return False

def repetido_subcuadrado(sudoku, fila, columna, numero):
    for i in range(3):
        for j in range(3):
            if sudoku[i + fila][j + columna] == numero:
                return True
    return False

def es_posible(sudoku, fila, columna, numero):
    return not repetido_fila(sudoku, fila, numero) and not repetido_columna(sudoku, columna, numero) and not repetido_subcuadrado(sudoku, fila - fila % 3, columna - columna % 3, numero)

def resolver_sudoku(sudoku):
    for fila in range(9):
        for columna in range(9):
            if sudoku[fila][columna] == 0:
                for numero in range(1, 10):
                    if es_posible(sudoku, fila, columna, numero):
                        sudoku[fila][columna] = numero
                        resolver_sudoku(sudoku)
                        sudoku[fila][columna] = 0
                return
    print(sudoku)


if __name__=="__main__":
    main()

