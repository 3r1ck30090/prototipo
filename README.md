# Proyecto

Como estoy iniciando haré algo básico como una calculadora usándola para cosas como en porcentajes o probabilidad (usando * y /), lo escojo porque necesito saber cómo funcionan los operadores aquí primero antes de realizar algo más grande.  
Además, funciona también como conversor las calculadoras solo agregando valores, solo que no he programado mucho, así que por mientras se quedará con operadores básicos como la suma, resta, multiplicación y división.  
He visto que hay comandos como `range` y con ellos puedo mejorar la calculadora siendo capaz de agregar estadística.
Pero despues de tanto aprender use todos los componentes que he visto hasta la fecha para que mi calculadore llegue hacer más cosas que operadores básicos aunque lo de random solo lo puse para que alguien tenga como un dado 
y pueda escoger algo por el de forma aleatoria pero de ahi use todos los componentes como listas y ciclos anidadas para las matrices lo unico que no he usado es el tema de archivos pero no encontre una manera de que se usen

## Algoritmo
`INICIO

Importar random, math y sys
REPETIR
    - Mostrar menú de opciones
    - Leer opción
    - SI opción = 1 → leer A, B → mostrar suma(A, B)
    - SI opción = 2 → leer A, B → mostrar resta(A, B)
    - SI opción = 3 → leer A, B → mostrar multiplicación(A, B)
   - SI opción = 4 → leer A, B → SI B ≠ 0 mostrar división(A, B)
   - SI opción = 5 → leer precio y porcentaje → mostrar descuento
   - SI opción = 6 → leer N → mostrar factorial(N)
   - SI opción = 7 o 8
       - Leer matriz 1
       - Leer matriz 2
       - SI tamaños diferentes → error
       - SI opción = 7 → sumar matrices y mostrar
       - SI opción = 8 → multiplicar matrices y mostrar
    - SI opción = 9 → leer lista y mostrar elemento aleatorio
    - SI opción = 10 → leer base y exponente → mostrar potencia
    - SI opción = 11 → leer número → mostrar raíz cuadrada
    - SI opción = 0
      -  Mostrar mensaje y salir
   - SI ninguna anterior
      -  Mostrar "opción no válida"
   - Preguntar si desea continuar (s/n)
- HASTA que respuesta ≠ "s"
Mostrar mensaje final `
---
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
 
