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
"""
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
else:
    print("The number is  zero")
"""

#============================================================================

# Exercise 13 — Conditionals for checking quadratic discriminant

# Problem:
# Create a program that asks the user to enter the coefficients (a, b, c)
# of a quadratic equation ax² + bx + c = 0.
# The program should calculate the discriminant (Δ = b² - 4ac)
# and show the type of solutions:
# - If Δ > 0 → show "Two real solutions".
# - If Δ == 0 → show "One real solution".
# - If Δ < 0 → show "No real solutions (complex roots)".

a = float(input("Enter  a number of coefficiente A: "))
b = float(input("Enter  a number of coefficiente B: "))
c = float(input("Enter  a number of coefficiente C: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    print("Two real solution")
elif discriminant  == 0 :
    print("One real solution")
elif discriminant < 0:
    print("No real solutions (Complex roots)")
"""

#============================================================================

# Ejercicio 14 — Condicionales para sistema de login básico
"""
# Problema:
# Crea un programa que simule un sistema de login simple.
# El programa debe pedir al usuario un nombre de usuario y contraseña,
# y verificar si coinciden con los valores almacenados:
# - Si ambos coinciden → mostrar "¡Login exitoso! Bienvenido/a".
# - Si el usuario es correcto pero la contraseña no → mostrar "Contraseña incorrecta".
# - Si el usuario no existe → mostrar "Usuario no encontrado".

# Este es un ejemplo práctico de cómo funcionan los sistemas de autenticación
# en aplicaciones reales como redes sociales, bancos, etc.

usuario_correcto = "admin"
contrasena_correcta = "12345"

usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("¡Login exitoso! Bienvenido/a")
elif usuario == usuario_correcto and contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intente nuevamente.")
else:
    print("Usuario no encontrado. Verifique su nombre de usuario.")
"""

#============================================================================

# Ejercicio 15 — Condicionales para clasificación de temperaturas
"""
# Problema:
# Crea un programa que pida al usuario ingresar una temperatura en grados Celsius
# y muestre un mensaje según el rango:
# - Si la temperatura es menor de 10 → mostrar "Hace mucho frío, abrígate bien".
# - Si está entre 10 y 20 → mostrar "El clima está fresco, usa una chaqueta ligera".
# - Si está entre 21 y 30 → mostrar "El clima está agradable, temperatura ideal".
# - Si es mayor de 30 → mostrar "Hace mucho calor, mantente hidratado/a".

# Este ejemplo es útil para aplicaciones del clima y sistemas de alerta.

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if temperatura < 10:
    print("Hace mucho frío, abrígate bien")
elif temperatura >= 10 and temperatura <= 20:
    print("El clima está fresco, usa una chaqueta ligera")
elif temperatura >= 21 and temperatura <= 30:
    print("El clima está agradable, temperatura ideal")
else:
    print("Hace mucho calor, mantente hidratado/a")
"""

#============================================================================

# Ejercicio 16 — Condicionales para cálculo de IMC (Índice de Masa Corporal)
"""
# Problema:
# Crea un programa que pida al usuario ingresar su peso en kilogramos y su altura en metros,
# calcule el IMC y muestre un mensaje según el resultado:
# - Si IMC < 18.5 → mostrar "Estás bajo de peso, consulta a un nutricionista".
# - Si IMC está entre 18.5 y 24.9 → mostrar "¡Tu peso es saludable! Continúa así".
# - Si IMC está entre 25 y 29.9 → mostrar "Tienes sobrepeso, cuida tu alimentación".
# - Si IMC >= 30 → mostrar "Tienes obesidad, busca orientación médica".

# Fórmula del IMC: peso / (altura * altura)
# Este ejemplo es muy útil en aplicaciones de salud y bienestar.

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estás bajo de peso, consulta a un nutricionista")
elif imc >= 18.5 and imc <= 24.9:
    print("¡Tu peso es saludable! Continúa así")
elif imc >= 25 and imc <= 29.9:
    print("Tienes sobrepeso, cuida tu alimentación")
else:
    print("Tienes obesidad, busca orientación médica")
"""

#============================================================================

# Ejercicio 17 — Condicionales para validar contraseña fuerte
"""
# Problema:
# Crea un programa que pida al usuario ingresar una contraseña
# y evalúe qué tan fuerte es según estos criterios:
# - Si tiene menos de 6 caracteres → mostrar "Contraseña muy débil".
# - Si tiene entre 6 y 8 caracteres → mostrar "Contraseña débil".
# - Si tiene entre 9 y 12 caracteres → mostrar "Contraseña moderada".
# - Si tiene más de 12 caracteres → mostrar "Contraseña fuerte".

# Este ejemplo es fundamental para aplicaciones de seguridad y protección de datos.

contrasena = input("Ingrese su contraseña: ")

longitud = len(contrasena)

if longitud < 6:
    print("Contraseña muy débil. Debe tener al menos 6 caracteres.")
elif longitud >= 6 and longitud <= 8:
    print("Contraseña débil. Considera hacerla más larga.")
elif longitud >= 9 and longitud <= 12:
    print("Contraseña moderada. Buen trabajo.")
else:
    print("Contraseña fuerte. ¡Excelente nivel de seguridad!")
"""

#============================================================================

# Ejercicio 18 — Condicionales para verificar si puede votar
"""
# Problema:
# Crea un programa que pida al usuario ingresar su edad
# y muestre un mensaje sobre su elegibilidad para votar:
# - Si es menor de 18 → mostrar "Aún no puedes votar, espera un poco más".
# - Si tiene entre 18 y 70 → mostrar "¡Puedes votar! Es tu derecho y deber cívico".
# - Si es mayor de 70 → mostrar "Puedes votar, pero es opcional para ti".

# Este ejemplo muestra cómo los condicionales se usan en sistemas legales y cívicos.

edad = int(input("Ingrese su edad: "))

if edad < 18:
    print("Aún no puedes votar, espera un poco más")
elif edad >= 18 and edad <= 70:
    print("¡Puedes votar! Es tu derecho y deber cívico")
else:
    print("Puedes votar, pero es opcional para ti")
"""

#============================================================================

# Ejercicio 19 — Condicionales para clasificación de triángulos
"""
# Problema:
# Crea un programa que pida al usuario ingresar las longitudes de tres lados de un triángulo
# y muestre qué tipo de triángulo es:
# - Si los tres lados son iguales → mostrar "Triángulo equilátero".
# - Si solo dos lados son iguales → mostrar "Triángulo isósceles".
# - Si todos los lados son diferentes → mostrar "Triángulo escaleno".
# - Si no puede formar un triángulo → mostrar "No es un triángulo válido".

# Para que sea un triángulo válido, la suma de dos lados debe ser mayor que el tercero.

lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

# Primero verificamos si puede ser un triángulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 and lado2 == lado3:
        print("Triángulo equilátero (todos los lados iguales)")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triángulo isósceles (dos lados iguales)")
    else:
        print("Triángulo escaleno (todos los lados diferentes)")
else:
    print("No es un triángulo válido")
"""

#============================================================================

# Ejercicio 20 — Condicionales para sistema de prioridades de tareas
"""
# Problema:
# Crea un programa que simule un sistema de prioridades para tareas.
# El usuario debe ingresar la urgencia de una tarea y mostrará su prioridad:
# - Si es "urgente" → mostrar "Prioridad ALTA - Debe hacerse inmediatamente".
# - Si es "importante" → mostrar "Prioridad MEDIA - Debe hacerse pronto".
# - Si es "normal" → mostrar "Prioridad BAJA - Puede esperar un poco".
# - Si es otro valor → mostrar "Categoría no reconocida".

# Este ejemplo es útil para aplicaciones de gestión de tareas y productividad.

urgencia = input("Ingrese la urgencia de la tarea (urgente/importante/normal): ").lower()

if urgencia == "urgente":
    print("Prioridad ALTA - Debe hacerse inmediatamente")
elif urgencia == "importante":
    print("Prioridad MEDIA - Debe hacerse pronto")
elif urgencia == "normal":
    print("Prioridad BAJA - Puede esperar un poco")
else:
    print("Categoría no reconocida. Use: urgente, importante o normal")
"""

#============================================================================

# Ejercicio 21 — Condicionales para verificar múltiplos
"""
# Problema:
# Crea un programa que pida al usuario ingresar dos números
# y verifique si el segundo número es múltiplo del primero:
# - Si el segundo número es múltiplo del primero → mostrar "Es múltiplo".
# - Si no es múltiplo → mostrar "No es múltiplo".

# Un número es múltiplo de otro si al dividirlo el residuo es 0.
# Este concepto es fundamental en matemáticas y programación.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if numero2 % numero1 == 0:
    print(f"{numero2} es múltiplo de {numero1}")
else:
    print(f"{numero2} no es múltiplo de {numero1}")
"""

#============================================================================

# Ejercicio 22 — Condicionales para clasificación de productos por precio
"""
# Problema:
# Crea un programa que pida al usuario ingresar el precio de un producto
# y muestre una categoría según su rango:
# - Si el precio es menor de 20 → mostrar "Producto económico".
# - Si está entre 20 y 50 → mostrar "Producto de precio medio".
# - Si está entre 51 y 100 → mostrar "Producto premium".
# - Si es mayor de 100 → mostrar "Producto de lujo".

# Este ejemplo es útil para sistemas de comercio electrónico y tiendas.

precio = float(input("Ingrese el precio del producto: "))

if precio < 20:
    print("Producto económico")
elif precio >= 20 and precio <= 50:
    print("Producto de precio medio")
elif precio >= 51 and precio <= 100:
    print("Producto premium")
else:
    print("Producto de lujo")
"""

#============================================================================

# Ejercicio 23 — Condicionales para determinar estación del año
"""
# Problema:
# Crea un programa que pida al usuario ingresar un número de mes (1-12)
# y muestre a qué estación del año pertenece:
# - Si es 12, 1 o 2 → mostrar "Invierno".
# - Si es 3, 4 o 5 → mostrar "Primavera".
# - Si es 6, 7 u 8 → mostrar "Verano".
# - Si es 9, 10 u 11 → mostrar "Otoño".
# - Si es otro número → mostrar "Mes no válido".

# Este ejemplo muestra cómo manejar múltiples condiciones con el mismo resultado.

mes = int(input("Ingrese el número del mes (1-12): "))

if mes == 12 or mes == 1 or mes == 2:
    print("Invierno")
elif mes == 3 or mes == 4 or mes == 5:
    print("Primavera")
elif mes == 6 or mes == 7 or mes == 8:
    print("Verano")
elif mes == 9 or mes == 10 or mes == 11:
    print("Otoño")
else:
    print("Mes no válido. Ingrese un número entre 1 y 12")
"""

#============================================================================

# Ejercicio 24 — Condicionales para sistema de calificación de restaurantes
"""
# Problema:
# Crea un programa que pida al usuario ingresar una calificación de restaurante (1-5)
# y muestre un mensaje según la calidad:
# - Si es 5 → mostrar "¡Excelente! Restaurante de primera categoría".
# - Si es 4 → mostrar "Muy bueno, recomendado".
# - Si es 3 → mostrar "Bueno, cumple con lo esperado".
# - Si es 2 → mostrar "Regular, podría mejorar".
# - Si es 1 → mostrar "Malo, no recomendado".
# - Si es otro valor → mostrar "Calificación no válida (debe ser 1-5)".

# Este ejemplo es útil para aplicaciones de reseñas y evaluación de servicios.
"""

calificacion = int(input("Ingrese la calificación del restaurante (1-5): "))

if calificacion == 5:
    print("¡Excelente! Restaurante de primera categoría")
elif calificacion == 4:
    print("Muy bueno, recomendado")
elif calificacion == 3:
    print("Bueno, cumple con lo esperado")
elif calificacion == 2:
    print("Regular, podría mejorar")
elif calificacion == 1:
    print("Malo, no recomendado")
else:
    print("Calificación no válida (debe ser 1-5)")
"""