"""
Proyecto Calculadora 
Simula una calculadora usando operadores básicos
y funciones más avanzadas para el usuario.
"""
# bibliotecas
import random
"""
esta bibloteca la use como especie de dado entre 
numeros que pida el usuario
"""
import math
"""
esta bibloteca la use para poder usar las potencias y 
las raices de un numero que guste el usuario 
"""
import sys
"""
esta bibloteca la use para poder usar funciones del sistema
y permiten interactuar directamente con el 
sistema donde se está ejecutando tu programa
lo use principalmente para salir del programa
"""
"""
operadores basicos
"""

def suma(a, b):
    """
    uso de operadores y funciones (a, b) 
    Suma dos valores numéricos y devuelve el resultado.
    """
    return a + b

def resta(a, b):
    """
    uso de operadores y funciones (a, b) 
    Resta dos valores numéricos y devuelve el resultado.
    """
    return a - b

def multiplicacion(a, b):
    """
    uso de operadores y funciones (a, b) 
    Multiplica dos valores numéricos y devuelve el resultado.
    """
    return a * b

def division(a, b):
    """
    uso de operadores, funciones y condicional (a, b) 
    Divide dos valores numéricos. Si el divisor es 0,
    devuelve un mensaje de error.
    """
    if b != 0:
        return a / b
    else:
        return "Error, no se puede dividir entre 0"

def descuento(a, b):
    """
    uso de operadores y funciones (a, b) 
    Calcula el descuento de un valor según el porcentaje dado.
    """
    return a * (b / 100)

def factorial(n):
    """
    uso de operadores, funciones, condicional y ciclos (n) 
    Calcula el factorial de un número. Si es negativo,
    devuelve un mensaje de error.
    """
    if n < 0:
        return "Error, no existe factorial de números negativos"
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1
    return resultado

def leer_matriz():
    """
    uso de funciones, listas, listas anadinas, ciclos y ciclos anidados
    Solicita al usuario crear una matriz 2x2 o 3x3
    y la devuelve como lista anidada.
    """
    n = int(input("Elige el tamaño: 2 para 2x2 o 3 para 3x3: "))
    print("Ingresa los valores de la matriz:")
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            valor = int(input(f"Valor [{i+1}][{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def suma_mat(a, b):
    """
    uso de operadores, funciones, listas, listas anidadas, ciclos
      ,ciclos anidadas
    Suma dos matrices del mismo tamaño y devuelve la matriz resultante.
    """
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def mult_mat(a, b):
    """
    uso de operadores, funciones, listas, listas anidadas, ciclos 
    ,ciclos anidadas
    Realiza multiplicación elemento a elemento de dos matrices
    y devuelve la matriz resultante.
    """
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] * b[i][j]
    return c

def imprimir_matriz(matriz):
    """
    uso de funciones, listas, listas anidadas, ciclos,
      ciclos anidadas
    Imprime una matriz fila por fila.
    """
    for fila in matriz:
        print(fila)

def num_random():
    """
    uso de funciones, listas, listas anidadas, ciclos, 
    ciclos anadidos y biblotecas
    Recibe valores del usuario y selecciona uno aleatoriamente.
    """
    n = int(input("¿Cuántos valores tendrá la lista?: "))
    lista = []

    for i in range(n):
        valor = input("Ingrese el valor: ")
        lista.append(valor)

    indice = int(random.random() * len(lista))
    print("Valor aleatorio elegido de la lista:", lista[indice])

def potencia(a, b):
    """
    uso de operadores y biblotecas
    Calcula la potencia de un número usando exponentes.
    """
    return pow(a, b)

def raiz_cuadrada(x):
    """
    usa operadores, condicionales y biblotecas 
    Calcula la raíz cuadrada de un número.
    Si es negativo, devuelve un mensaje de error.
    """
    if x < 0:
        return "Error: no se puede calcular raíz de número negativo"
    return math.sqrt(x)

while True:
    print(" Escoge una de las opciones que necesite")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Descuento")
    print("6. Factorial")
    print("7. Suma de Matrices")
    print("8. Multiplicación de Matrices")
    print("9. Elecciones random")
    print("10. Potencia")
    print("11. Raices")
    print("0. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "0":
        print("Nos vemos luego, vaquero.")
        sys.exit()

    if opcion in ["1", "2", "3", "4"]:
        a = int(input("Número 1: "))
        b = int(input("Número 2: "))

        if opcion == "1":
            print("Resultado de la suma:", suma(a, b))
        elif opcion == "2":
            print("Resultado de la resta:", resta(a, b))
        elif opcion == "3":
            print("Resultado de la multiplicación:", multiplicacion(a, b))
        elif opcion == "4":
            while b == 0:
                print("No se puede dividir entre 0, intenta de nuevo.")
                b = int(input("Número 2: "))
            print("Resultado de la división:", division(a, b))
    elif opcion == "5":
            a = int(input("¿Cúal es el precio original?: "))
            b = int(input("¿Cúal es el porcentaje de descuento?: "))
            print("El descuento seria de:", descuento(a, b))

    elif opcion == "6":
        n = int(input("Introduce un número para calcular su factorial: "))
        print("Factorial:", factorial(n))

    elif opcion in ["7", "8"]:
        mat1 = leer_matriz()
        mat2 = leer_matriz()

        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            print("No es posible operar con matrices de diferente tamaño")
        else:
            if opcion == "7":
                print("Resultado de la suma de matrices:")
                imprimir_matriz(suma_mat(mat1, mat2))
            if opcion == "8":
                print("Resultado de la multiplicación de matrices:")
                imprimir_matriz(mult_mat(mat1, mat2))

    elif opcion == "9":
        num_random()

    elif opcion == "10":
        a = int(input("¿Cúal número quieres elevar?: "))
        b = int(input("¿Cúal sera su potencia?: "))
        print("Potencia:", potencia(a, b))

    elif opcion == "11":
        x = int(input("¿Cúal número quiere conocer su raiz?: "))
        print("La raiz es:", raiz_cuadrada(x))

    else:
        print("Opción no válida.")
    
    continuar = input("¿Deseas realizar otra operación? (s/n): ")
    if continuar != "s":
        print("Eso Eso Eso es todo amigos")
        sys.exit()


