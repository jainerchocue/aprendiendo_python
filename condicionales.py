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

"""
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
"""

#============================================================================

# Ejercicio 6 — Condicionales para verificar el mayor de tres números

"""
# Problema:
# Crea un programa que pida al usuario ingresar tres números
# y muestre un mensaje indicando cuál es el mayor:
# - Si el primer número es el mayor → mostrar "El primer número es el mayor".
# - Si el segundo número es el mayor → mostrar "El segundo número es el mayor".
# - Si el tercer número es el mayor → mostrar "El tercer número es el mayor".
# - Si los tres números son iguales → mostrar "Los tres números son iguales".

numero1 = float(input("Ingrese el primero valor: "))
numero2 = float(input("Ingrese el segundo valor: "))
numero3 = float(input("Ingrese el tercer valor: "))

if numero1 > numero2 and numero1 > numero3:
    print("El primer numero es el mayor")
elif numero2 > numero1 and numero2 > numero3:
    print("El segundo numero es el mayor")
elif numero3 > numero1 and numero3 > numero2:
    print("El tercer numero es el mayor")
else:
    print("Los tres numeros son iguales")
"""


#============================================================================

# Ejercicio 7 — Condicionales para verificar si un año es bisiesto

"""
# Problema:
# Crea un programa que pida al usuario ingresar un año
# y muestre un mensaje indicando si es bisiesto o no:
# - Un año es bisiesto si es divisible por 4.
# - Pero si es divisible por 100, no es bisiesto.
# - Sin embargo, si es divisible por 400, sí es bisiesto.
# Ejemplo: 2000 es bisiesto, 1900 no lo es, 2024 sí lo es.

year = int(input("Ingresar un año: "))

if year % 400 == 0:  
    print("El año es bisiesto")  # divisible por 400 → siempre bisiesto
elif year % 100 == 0:  
    print("El año no es bisiesto")  # divisible por 100 → no bisiesto
elif year % 4 == 0:  
    print("El año es bisiesto")  # divisible por 4 → bisiesto
else:
    print("El año no es bisiesto")  # cualquier otro caso → no bisiesto
"""

#============================================================================

# Exercise 8 — Conditionals for calculating purchase discounts

"""
# Problem:
# Create a program that asks the user to enter the total amount of a purchase
# and shows the final price after applying a discount:
# - If the amount is less than 100 → no discount.
# - If the amount is between 100 and 500 → apply a 10% discount.
# - If the amount is greater than 500 → apply a 20% discount.


amount = int(input("Enter the value of amount of a purchase: "))

if amount < 100:
    print("No discount")
elif amount >= 100 and amount < 500:
    discount = amount*0.1
    final_price = amount - discount
    print(f"10% discount applied. Final price  is {final_price}")
elif amount >= 500:
    discount = amount*0.2
    final_price = amount - discount
    print(f"20% discount applied. Final price  is {final_price}")
"""

#============================================================================

# Exercise 9 — Conditionals for grading system
"""
# Problem:
# Create a program that asks the user to enter a score (0 to 100)
# and shows the corresponding grade:
# - If the score is 90 or above → show "Grade A".
# - If the score is between 80 and 89 → show "Grade B".
# - If the score is between 70 and 79 → show "Grade C".
# - If the score is between 60 and 69 → show "Grade D".
# - If the score is below 60 → show "Grade F".

score = int(input("Enter a score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score >=0 and score <= 59:
    print("Grade F")
else:
    print("The value is outsite of the range")
"""

#============================================================================

# Exercise 10 — Conditionals for a simple calculator
"""
# Problem:
# Create a program that asks the user to enter two numbers
# and then choose an operation (add, subtract, multiply, divide).
# The program should show the result according to the chosen operation:
# - If the user chooses "add" → show the sum of the two numbers.
# - If the user chooses "subtract" → show the difference.
# - If the user chooses "multiply" → show the product.
# - If the user chooses "divide" → show the division result.
# - If the user enters an invalid operation → show "Invalid operation".

numbers1 = float(input("Enter the first numbers: "))
numbers2 = float(input("Enter the secund numbers: "))
opcion = input("Enter the opcion: ")

if opcion == "add":
    add = numbers1 + numbers2
    print(f"The value of add is {add}")
elif opcion == "subtract":
    subtract = numbers1 - numbers2
    print(f"The value of subtract is {subtract}")
elif opcion == "multiply":
    multiply = numbers1 * numbers2
    print(f"The value of multiply is {multiply}")
elif opcion == "divide":
    if numbers2 == 0:
        print("zero divide error")
    else:
        divide = numbers1 / numbers2
        print(f"The value of divide is {divide}")
else:
    print("Invalid operation")
"""


#============================================================================

# Exercise 11 — Conditionals for checking vowels and consonants
"""
# Problem:
# Create a program that asks the user to enter a single letter
# and shows whether it is a vowel or a consonant:
# - If the letter is 'a', 'e', 'i', 'o', or 'u' → show "It is a vowel".
# - If the letter is any other alphabet character → show "It is a consonant".
# - If the input is not a letter → show "Invalid input".

letter = input("Enter a single letter: ")

vowel = 'a,e,i,o,u'

if letter in vowel:
    print("It is a vowel")
elif letter.isalpha() and len(letter) == 1:
    print("It is a consonant")
else:
    print("Invalid input")
"""


#============================================================================

# Exercise 12 — Conditionals for checking positive, negative, or zero

# Problem:
# Create a program that asks the user to enter a number
# and shows whether the number is positive, negative, or zero:
# - If the number is greater than 0 → show "The number is positive".
# - If the number is less than 0 → show "The number is negative".
# - If the number is equal to 0 → show "The number is zero".


number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
elif number == 0:
    print("The number is  zero")
