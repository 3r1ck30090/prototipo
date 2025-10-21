# Proyecto
Como estoy iniciando haré algo básico como una calculadora usándola para cosas como en porcentajes o probabilidad (usando * y /), lo escojo porque necesito saber cómo funcionan los operadores aquí primero antes de realizar algo más grande.  
Además, funciona también como conversor las calculadoras solo agregando valores, solo que no he programado mucho, así que por mientras se quedará con operadores básicos como la suma, resta, multiplicación y división.  
He visto que hay comandos como `range` y con ellos puedo mejorar la calculadora siendo capaz de agregar estadística.

---

## Algoritmo
- Mostrar “Calculadora básica”  
- Ingresar el primer número/valor  
- Escoger la operación (suma, resta, multiplicación, división)  
- Ingresar el segundo número/valor  
- Si la operación es igual a suma → colocar `+`  
- Si la operación es igual a resta → colocar `-`  
- Si la operación es igual a multiplicación → colocar `*`  
- Si la operación es igual a división → colocar `/`  
- Resultado = (num1 + num2, num1 - num2, num1 * num2, num1 / num2)  
- Si `num2 = 0` imprimir “no es posible dividir en 0”  
- Volver a `num2` y volver a escribir


## Con código sería como

``python
- print('calculadora')
- num1 = float(input('ingresa el primer número'))
- operacion = input('qué operación quieres usar (suma, resta, multiplicación, división)')
- num2 = float(input('ingresa el segundo número'))

- if operacion == 'suma':
  -  res = num1 + num2
- if operacion == 'resta':
 -   res = num1 - num2
- if operacion == 'multiplicación':
 -   res = num1 * num2
- if operacion == 'división':
 -   res = num1 / num2

- print('resultado es =', res)



# CALCULADORA
contexto esta idea surgio porque fue lo más basico que se me ocurrio, ademas desde el inicio de las matematicas en el siglo VVII fue algo que se creo solo con operadores basicos como las sumas y restas 
ademas tiene varias interacciones:
- Entrada del usuario: aqui el usuario elige lo que gusta calcular
- Procesamiento interno: aqui el programa con los datos del usuario 
- Cálculos: aqui hay operadores basicos, operaciones de grado 2 y con biblotecas sacadas de [(random.random)](https://docs.python.org/es/3.13/library/random.html) , [(pow)](https://docs.python.org/3/library/functions.html#pow) y [(math.sqrt) ](https://docs.python.org/3/library/math.html#math.sqrt) pude hacer que las raices funcionen , que el mismo codigo saque un numero aleatorio y usar el pow para poder usar potencias  
- Salida o resultado: al final saca el resultado del problema que el usuario tenga 

# INSTRUCCIONES
Descargar el arvhivo y correr en terminal con:
Proyect.py
abrir en Thonny y dar boton de play.
