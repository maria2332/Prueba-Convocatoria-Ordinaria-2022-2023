"""
Crea función que calcula el millonésimo número en la recurrencia de Fibonacci, sabiendo que debe usar un algoritmo iterativo para calcular el millonésimo número en la recurrencia de Fibonacci.Para ello ejecute los siguientes pasos
Primero, se inicializan los dos primeros números en la recurrencia (0 y 1).
Luego, se calculan los números sucesivos en la recurrencia usando la fórmula c = a + b, donde c es el número en la posición n, a es el número en la posición n - 1 y b es el número en la posición n - 2.
Este proceso se repite hasta llegar al millonésimo número en la recurrencia, que se devuelve como resultado.
Escriba un algoritmo que pueda manejar n hasta 2000000.
Su algoritmo debe generar la respuesta entera exacta, con total precisión. Además, debe manejar correctamente los números negativos como entrada.
"""

import ast as main 
import numpy as np

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterativo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    main()