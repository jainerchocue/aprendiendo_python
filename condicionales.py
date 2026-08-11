# 📘 El uso de Condicionales en ProgramaciónBienvenido/a a este espacio. 
# El objetivo de este código es mostrar el funcionamiento de las estructuras condicionales.Una condicional es un proceso que otorga a las computadoras la capacidad de tomar decisiones lógicas. 
# Al evaluar el flujo del programa, el sistema escoge la ruta que cumple con los requisitos establecidos y, en caso contrario, ejecuta un camino alternativo. 
# Comprender esta técnica es crucial para dominar los fundamentos del desarrollo de software.

#============================================================================

# Ejercicio 1 — Condicionales básicos para evaluar edades
"""
# Tema: Condicionales en Python (if, elif, else)
# Los condicionales permiten que un programa tome decisiones
# dependiendo de los valores que recibe."""

"""
# Problema:
# Crea un programa que pida al usuario ingresar su edad
# y muestre un mensaje según el rango:
# - Si la edad es menor de 18 → mostrar "Eres menor de edad".
# - Si la edad está entre 18 y 65 → mostrar "Eres adulto".
# - Si la edad es mayor de 65 → mostrar "Eres adulto mayor".


edad = int(input("Ingrese la edad: "))  # es int porque la edad es un valor entero

# estamos diciendo que si edad es menor a 18, es menor de edad
if edad < 18: 
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:  
    # acá se evalúa el intervalo de edad y si la edad entra en eso, cumple
    print("Eres adulto")
else:  
    # y si la edad ya es mayor o igual, ejecuta esta parte
    print("Eres adulto mayor")
"""

#============================================================================

# Ejercicio 2 — Condicionales anidados para clasificar notas escolares
"""
# Problema:
# Crea un programa que pida al usuario ingresar una nota (0 a 100)
# y muestre un mensaje según el rango:
# - Si la nota es mayor o igual a 90 → mostrar "Excelente".
# - Si la nota está entre 70 y 89 → mostrar "Bueno".
# - Si la nota está entre 50 y 69 → mostrar "Regular".
# - Si la nota es menor de 50 → mostrar "Insuficiente".

nota = float(input("Ingrese  la nota de 0 a 100: "))

if nota < 50:
    print("Insuficiente")
elif nota >= 50 and  nota <= 69:
    print("Regular")
elif nota >= 70 and nota <=89:
    print("Bueno")
elif nota>=90 and nota <= 100: 
    print("Excelente")
else:
    print("El valor de la nota esta fuera del rango de 0 a 100")
"""

#============================================================================

# Ejercicio 3 — Condicionales para verificar números pares e impares
"""
# Problema:
# Crea un programa que pida al usuario ingresar un número entero
# y muestre un mensaje según el caso:
# - Si el número es par → mostrar "El número es par".
# - Si el número es impar → mostrar "El número es impar".

numero = int(input("Ingrese un numero entero: "))

if numero%2==0: # en esta parte utilizamos el modal , para poder extraer el residuo, y si el residuou es cero, eso indica que es par.
    print("El numero es par")
else: # si no comple con lo anterior, entonces indica que es impar
    print("El numero es impar")
"""

#============================================================================

# Ejercicio 4 — Condicionales para verificar números positivos, negativos o cero
"""
# Problema:
# Crea un programa que pida al usuario ingresar un número
# y muestre un mensaje según el caso:
# - Si el número es mayor que 0 → mostrar "El número es positivo".
# - Si el número es menor que 0 → mostrar "El número es negativo".
# - Si el número es igual a 0 → mostrar "El número es cero".

numero = float(input("Ingrese un numero: "))

if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0:
    print(f"EL numero que ingresaste es {numero}")
elif numero < 0:
    print(f"El numero {numero} es negativo")
 """  

#============================================================================

# Ejercicio 5 — Condicionales para verificar el mayor de dos números

# Problema:
# Crea un programa que pida al usuario ingresar dos números
# y muestre un mensaje indicando cuál es mayor o si son iguales:
# - Si el primer número es mayor → mostrar "El primer número es mayor".
# - Si el segundo número es mayor → mostrar "El segundo número es mayor".
# - Si ambos son iguales → mostrar "Ambos números son iguales".

numero1 = float(input("Ingrese el primer valor: "))
numero2 = float(input("Ingrese el segundo valor: "))

if numero1 > numero2:
    print(f"El primer numero {numero1} es mayor al segundo numero {numero2}")
elif numero2 > numero1:
    print(f"El numero segundo numero  {numero2} es mayor al primer numero {numero1}")
else:
    print(f"El primer numero {numero1} es igual al segundo numero {numero2}")