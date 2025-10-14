"""
Proyecto Calculadora 
El proyecto trata de simular como una calculadora 
y darle al usuario lo que quiera que este a su alcance usando operadores basicos
o funciones más avanzadas
"""
#bibliotecas
import random
"""
esta bibloteca la use como especie de dado entre numeros que pida el usuario
"""
import math
"""
esta bibloteca la use para poder usar las potencias y las raices de un numero que guste el usuario 
"""
"""
operadores basicos
"""
def suma(a, b):
    """
    uso de operadores y funciones (a, b) 
    pide a valor númerico  y b valor númerico
    el programa suma a y b y devuelve el resultado de dicha operacion
    """
    return a + b

def resta(a, b):
    """
    uso de operadores y funciones (a, b) 
    pide a valor númerico  y b valor númerico
    el programa resta a y b y devuelve el resultado de dicha operacion
    """
    return a - b

def multiplicacion(a, b):
    """
    uso de operadores y funciones (a, b) 
    pide a valor númerico  y b valor númerico
    el programa multiplica a y b y devuelve el resultado de dicha operacion
    """
    return a * b

def division(a, b):
    """
    uso de operadores, funciones y condicional (a, b) 
    pide a valor númerico  y b valor númerico
    el programa y a y b y devuelve el resultado de dicha operacion y si termina una division
    matematicamente imposible devuelve error 
    """
    if b != 0:
        return a / b
    else:
        return "Error, no se puede dividir entre 0"

def porcentaje(a, b):
    """
    uso de operadores y funciones (a, b) 
    pide a valor númerico  y b valor númerico
    el programa usa a como el valor principal y b como el porcentaje y devuelve el resultado de dicha operacion
    """
    return a * (b / 100)

def factorial(n):
    """
    uso de operadores, funciones, condicional y ciclos (n) 
    pide a valor númerico 
    el programa usa n como el numero con el factorial, si el usuario pide numeros negativos marcara error al no ser posible y utilizando ciclos
    va restando su mismo numero para ir multiplicando
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
    pide n valor de escala y pide i y j como valores de escala y numerico pidiendo al usuario escribir su propia matriz
    el programa con los datos dados crea la matriz y la guarda para que el usuario la pueda sumar o multiplicar 
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
    uso de operadores, funciones, listas, listas anidadas, ciclos ,ciclos anidadas
    usando la matriz que fue solicitada en la anterior funcion suma la matriz de fila a columna (i, j) y más adelante si el tamaño es distinto 
    marcara error al no ser posible 
    usando n de la anterior funcion para ver la matriz guardada
    """
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c

def mult_mat(a, b):
    """
    uso de operadores, funciones, listas, listas anidadas, ciclos ,ciclos anidadas
    usando la matriz que fue solicitada en la anterior funcion multiplica la matriz de fila a columna (i, j) 
    usando n de la anterior funcion para ver la matriz guardada
    """
    n = len(a)
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] * b[i][j]
    return c

def imprimir_matriz(matriz):
    """
    uso de funciones, listas, listas anidadas, ciclos, ciclos anidadas
    despues de que la matriz dada y calculada esta funcion imprime el resultado de dicha matriz si es posible 
    """
    for fila in matriz:
        print(fila)

def num_random():
    """
    uso de funciones, listas, listas anidadas, ciclos, ciclos anadidos y biblotecas
    recibe n como el total de numeros en la lista y valor para el tener esos numeros aleatorios o no que de el usuario para devolver 
    en esa lista un numero al azar 
    """
    n = int(input("¿Cuántos números tendrá la lista?: "))
    lista = []

    for i in range(n):
        valor = input("Ingrese los número: ")
        lista.append(valor)

    indice = int(random.random() * len(lista))
    print("Número aleatorio elegido de la lista:", lista[indice])

def potencia(a, b):
    """
    uso de operadores y biblotecas
    recibe a como el numero y b como la potencia 
    devuelve la potencia de dicho numero 
    """
    return pow(a, b)

def raiz_cuadrada(x):
    """
    usa operadores, condicionales y biblotecas 
    recibe x como el numero que quieren sacar la raiz 
    y si ese numero llega a ser negativo devuelve error
    si no devuelve la raiz de dicho numero
    """
    if x < 0:
        return "Error: no se puede calcular raíz de número negativo"
    return math.sqrt(x)

print(" Escoge una de las opciones que necesite")
print("\n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Porcentaje")
print("6. Factorial")
print("7. Suma de Matrices")
print("8. Multiplicación de Matrices")
print("9. Número random")
print("10. Potencia")
print("11. Raices")
print("\n")
opcion = input("Elige una opción: ")
"""
Lista de opciones para elegir
"""
"""
usando condicional dependiendo de la opcion elegida usa una funcion y con una lista guarda los operadores basicos [1 , 2 , 3, 4 , 5] que usan 
solo 2 variables (a, b) para facilitar y no andar poniendo variables a cada funcion 
y si es distinto a los operadores basico usa otras funciones y operadores y si pone otro numero que no este marca invalido 
"""
if opcion in ["1", "2", "3", "4", "5"]:
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))

    if opcion == "1":
        print("Resultado de la suma:", suma(a, b))
    elif opcion == "2":
        print("Resultado de la resta:", resta(a, b))
    elif opcion == "3":
        print("Resultado de la multiplicación:", multiplicacion(a, b))
    elif opcion == "4":
        """
        con ciclos si el usuario como al dividendo como 0 lo devolvera la opcion para que cambie de numero 
        y seguira asi hasta que el 0 no este en la variable
        """
        while b == 0:
            print("No se puede dividir entre 0, intenta de nuevo.")
            b = int(input("Número 2: "))
        print("Resultado de la división:", division(a, b))
    elif opcion == "5":
        print("Resultado del porcentaje:", porcentaje(a, b))
elif opcion == "6":
    n = int(input("Introduce un número entero para calcular su factorial: "))
    print("Factorial:", factorial(n))

elif opcion in ["7", "8"]:
    mat1 = leer_matriz()
    mat2 = leer_matriz()

    if opcion == "7":
        """
        con condicional se usa como limite para las matrizes porque si la matriz es distinta de tamaño
        no podra sumar
        """
        if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
            print("No es posible operar con matrices de diferente tamaño")
        else:
            print("Resultado de la suma de matrices:")
            imprimir_matriz(suma_mat(mat1, mat2))
    if opcion == "8":
        print("Resultado de la multiplicación:")
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
