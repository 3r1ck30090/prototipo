def calculadora(a, b):
    print("\nResultados:")

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

print("Prueba de operaciones básicas")
print("Pon dos números para calcular:")
a = float(input("Número 1: "))
b = float(input("Número 2: "))

calculadora(a, b)