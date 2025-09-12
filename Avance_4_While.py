def calculadora(a, b):
    print("Resultados:")

    if b != 0:
        division = a / b
        print("División: %.2f" % division)
    else:
        print("División: Error, no se puede dividir entre 0")
    
    multiplicacion = a * b
    print("Multiplicación:", int(multiplicacion))
    
    suma = a + b
    print("Suma: %.2f" % suma)

    resta = a - b
    print("Resta: %.2f" % resta)

    porcentaje = a * (b / 100)
    print("Porcentaje: %.2f" % porcentaje)


def factorial(n):
    if n < 0:
        return "Error, no existe factorial de números negativos"
    resultado = 1
    while n > 1:
        resultado = resultado * n
        n = n - 1
    return resultado


print("Prueba de operaciones básicas")
print("Pon dos números para calcular:")
a = float(input("Número 1: "))
b = float(input("Número 2: "))

calculadora(a, b)

print("Calculo de factorial")
n = int(input("Introduce un número entero para calcular su factorial: "))
print("Factorial:", factorial(n))