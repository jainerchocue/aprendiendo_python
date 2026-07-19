# Ejercicio 1 — Calculadora básica
"""
#Crea dos variables con números.
#Haz las operaciones de suma, resta, multiplicación y división.
#Imprime cada resultado en un mensaje claro.

numero1 = 10
numero2 = 20

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2  
division = numero1 / numero2 # el numero2 debe ser diferente de cero(0)

print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicación es: {multiplicacion}")
print(f"La división es: {division}")
"""

# =======================================================

# Ejercicio 2 — Potencia y raíz cuadrada
"""
# Crea una variable numero.
# Calcula el cuadrado de ese número y su raíz cuadrada.
# Imprime los resultados en mensajes como:
# El cuadrado de ___ es ___  
# La raíz cuadrada de ___ es ___

numero = 50
cuadrado = numero**2 # para sacar el cuadrado se eleva a 2 con doble asterisco (**) 
raiz_cuadrada = numero**0.5  # para sacar raiz cuadra se eleva a 0.5 con doble asterisco (**) 

print(f"El cuadrado de {numero} es {cuadrado}")
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
"""

# =======================================================

# Ejercicio 3 — Módulo y división entera
"""
# Crea dos variables con números enteros.
# Calcula el módulo (%) y la división entera (//).
# Imprime los resultados en mensajes como:
# El módulo de ___ y ___ es ___  
# La división entera de ___ entre ___ es ___

numero1= 10
numero2 = 3

modulo = numero1 % numero2 # La funcion del modulo (%) es ayudar a obtener el residuo de una division, Por ejemplo 10 % 3 = 1
division_entera = numero1 // numero2 # La funcion de la division entera (//) es ayudar a obtener el cociente de una division, Por ejemplo 10 // 3 = 3

print(f"El módulo de {numero1} y {numero2} es {modulo}")
print(f"La división entera de {numero1} entre {numero2} es {division_entera}")
"""

# =======================================================

# Ejercicio 4 — Promedio con operaciones

#Crea tres variables con números.
#Calcula el promedio usando operaciones matemáticas.
#Imprime el resultado en un mensaje como:
#El promedio de ___, ___ y ___ es ___

valor1 = 10
valor2 = 8
valor3 = 9

promedio = (valor1 + valor2 + valor3) / 3

print(f"El promedio de {valor1}, {valor2} y {valor3} es: {promedio}")