# Proyecto
Como estoy iniciando haré algo básico como una calculadora usándola para cosas como en porcentajes o probabilidad (usando * y /), lo escojo porque necesito saber cómo funcionan los operadores aquí primero antes de realizar algo más grande.  
Además, funciona también como conversor las calculadoras solo agregando valores, solo que no he programado mucho, así que por mientras se quedará con operadores básicos como la suma, resta, multiplicación y división.  
He visto que hay comandos como `range` y con ellos puedo mejorar la calculadora siendo capaz de agregar estadística.

---

## Algoritmo
## 📌 Importación de Bibliotecas
- `random`
- `math`
- `sys`
##  Funciones Básicas

###  Función `suma(a, b)`
Retorna:
- a + b
### Función `resta(a, b)`
Retorna:
- a - b
### Función `multiplicación(a, b)`
Retorna:
- a * b
### Función `división(a, b)`
Condiciones:
- Si `b ≠ 0` → retornar `a / b`
- Si no → retornar error
### Función `descuento(a, b)`
Retorna:
- a * (b / 100)
## Función `factorial(n)`
Condiciones:
- Si `n < 0` → retornar error
- Proceso:
- resultado = 1
- Mientras n > 1:
- resultado = resultado * n
- n = n - 1
- Retornar resultado
## Función `leer_matriz()`
- 1. Solicitar tamaño (2 o 3)
- 2. Crear matriz vacía
- 3. Para cada fila y columna:
   - Pedir valor al usuario
   - Guardar
- 4. Retornar matriz
## Función `suma_mat(a, b)`
Proceso:
- Crear matriz resultado
- Para i y j:
- resultado[i][j] = a[i][j] + b[i][j]
- Retornar resultado
## Función `mult_mat(a, b)`
Proceso:
- Crear matriz resultado
- Para i y j:
- resultado[i][j] = a[i][j] * b[i][j]
- Retornar resultado
## Función `imprimir_matriz(matriz)`
Proceso:
- Para cada fila:
- imprimir fila
## Función `num_random()`
- 1. Solicitar cantidad de valores
- 2. Leer valores y agregarlos a una lista
- 3. Generar índice aleatorio
- 4. Mostrar elemento seleccionado
## Función `potencia(a, b)`
Retorna:
- pow(a, b)
## Función `raiz_cuadrada(x)`
Condiciones:
- Si `x < 0` → retornar error
- Si no → retornar:
math.sqrt(x)
##  Bucle Principal
Repetir SIEMPRE mostrando menú:
- Suma
- Resta
- Multiplicación
- División
- Descuento
- Factorial
- Suma de matrices
- Multiplicación de matrices
- Elección random
- Potencia
- Raíz
- Salir
## Validación de Opciones
### `0` → Salir
- Mostrar mensaje
- Terminar programa
### `1 a 4` → Operaciones básicas
- Pedir número A
- Pedir número B
- Realizar operación
- Mostrar resultado
### `5` → Descuento
- Pedir precio original
- Pedir porcentaje
- Mostrar resultado
### `6` → Factorial
- Pedir número
- Mostrar resultado
### `7` y `8` → Operaciones con matrices
- Leer primera matriz
- Leer segunda matriz
- Si tamaños diferentes → error
#### `7`: Sumar matrices
- Mostrar resultado
#### `8`: Multiplicar matrices
- Mostrar resultado
### `9` → Elección aleatoria
- Ejecutar `num_random()`
### `10` → Potencia
- Pedir base
- Pedir exponente
- Mostrar resultado
### `11` → Raíz cuadrada
- Pedir número
- Mostrar resultado
### Otra opción:
- Mostrar: “Opción no válida”
##  Después de cada operación:
¿Deseas realizar otra operación? (s/n)
- Si respuesta ≠ `s`:
  - Mostrar mensaje de despedida
  - Salir del programa
### Fin del Programa
# CALCULADORA
contexto esta idea surgio porque fue lo más basico que se me ocurrio, ademas desde el inicio de las matematicas en el siglo VVII fue algo que se creo solo con operadores basicos como las sumas y restas 
ademas tiene varias interacciones:
- Entrada del usuario: aqui el usuario elige lo que gusta calcular
- Procesamiento interno: aqui el programa con los datos del usuario 
- Cálculos: aqui hay operadores basicos, operaciones de grado 2 y con biblotecas sacadas de [(random.random)](https://docs.python.org/es/3.13/library/random.html) , [(pow)](https://docs.python.org/3/library/functions.html#pow), [(sys)](https://docs.python.org/3/library/sys.html) y [(math.sqrt) ](https://docs.python.org/3/library/math.html#math.sqrt) pude hacer que las raices funcionen , que el mismo codigo saque un numero aleatorio, poder hacer que el sistema cierre cuando el usuario quiera  y usar el pow para poder usar potencias  
- Salida o resultado: al final saca el resultado del problema que el usuario tenga 

# INSTRUCCIONES
- Descargar el arvhivo y correr en terminal con:
- Proyect.py
- abrir en Thonny y dar boton de play.
 
