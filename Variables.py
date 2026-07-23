###### FASE 1 #####
# Ejercicio 1: Crea dos variables, una para tu nombre y otra para tu edad. 


# Luego imprime un mensaje que diga: "Mi nombre es ___ y tengo ___ años."
"""

nombre = "Juan"
edad = 25
# Primera forma de hacerlo con + variable +  par  imprimir junto con el mensaje
print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.") 
# Segunda forma de hacerlo con f-string y imprimir junto con le mensaje es colocar f y despues adentro con los {variable}
print(f"Mi nombre es {nombre} y tengo {edad} años.")
"""

# ===================================================================================

# Ejercicio 2: Crea una variable que guarde una temperatura en grados Celsius.
"""
# Convierte esa temperatura a Fahrenheit usando la fórmula F = C * 9/5 + 32.
# Imprime el resultado en un mensaje como: "La temperatura en Fahrenheit es ___."

celsius = 50
fanrenheit = celsius * 9/5 + 32
print(f"La temperatura en Fahrenheit es {fanrenheit}.")
"""

# ===================================================================================

#Ejercicio 3 — Área de un rectángulo
"""
# Calcula el área de un rectángulo usando la fórmula: Área = base * altura.
# Imprime el resultado en un mensaje como: "El área del rectángulo es ___."

base = 10
altura = 10
area = base * altura
print(f"El área del rectángulo es {area}.")
"""

# ===================================================================================

# Ejercicio 4 -- Promedio de notas
"""
# Calcula el promedio de esas notas y muestra el resultado en un mensaje como:
# "El promedio de las notas es ___."
nota1 = 80
nota2 = 90
nota3 = 70

promedio = (nota1 + nota2 + nota3) /3 # se divide por la cantidad de notas
print(f"El promedio de las notas es {promedio}.")
"""

# ===================================================================================

# Ejercicio 5 — Intercambio de valores

# Intercambia sus valores y muestra los resultados antes y después.

# --- FORMA 1: Usando una variable auxiliar (Método tradicional) ---
"""
a = 10
b = 5
print(f"EL valor de 'a' antes del intercambio: {a}")
print(f"EL valor de 'b' antes del intercambio: {b}")

c = a 
a = b
b = c
print(f"EL valor de 'a' despues del intercambio: {a}")
print(f"EL valor de 'b' despues del intercambio: {b}")
"""

# --- FORMA 2: El truco de magia de Python (En una sola línea) ---
"""
x = 10
y = 5

x,y = y,x 
print(f"Ahora 'x' vale: {x}") # Imprime 5
print(f"Ahora 'y' vale: {y}") # Imprime 10
"""
# ===================================================================================

# Ejercicio 6: Crea variables para nombre, edad, ciudad y hobby favorito.
"""
# Imprime un mensaje que combine toda esa información en una sola frase.

nombre = "Juan"
edad = 20
ciudad = "Bogota"
hobby_favorito = "Aprender a programar"

print(f"Me llamo {nombre}, tengo {edad} años, vivo en {ciudad} y me gusta {hobby_favorito}")
"""

# ===================================================================================

# Ejercicio 7: Crea variables para el precio de un producto y la cantidad comprada.
"""
precio_producto = 10000 # cop -> colombia-> pesos
cantidad_compra = 5
total_pagar = precio_producto * cantidad_compra

print(f"Compraste {cantidad_compra} unidades, cada una cuesta: {precio_producto}, el total a pagar es: {total_pagar}")
"""

# ===================================================================================

# Ejercicio 8: Crea variables para nombre_jugador, nivel, puntos_experiencia y vida de un videojuego
"""
nombre_jugador = "Juan"
nivel = 6 # 0 = basico, 5 medio , 10 muy bueno
puntos_experiencia = 7 # 0 a 10
vida = 3 #0 a 5 -> oportunidades

print(f"Jugador {nombre_jugador} esta en el nivel {nivel} con {puntos_experiencia} puntos de experiencia y {vida} de vida")

"""
# ===================================================================================

# Ejercicio 9: Crea variables para nombre_cliente, producto, precio_unitario y cantidad.
"""
nombre_cliente = "sandra campo"
producto = "manzanas"
precio_unitario = 1000 # pesos colombianos
cantidad= 10
total = precio_unitario * cantidad

print(f"Cliente {nombre_cliente} compro {cantidad} unidades de {producto}, cada una cuesta $: {precio_unitario}, el total a pagar es $: {total}")
"""

# ===================================================================================

# Ejercicio 10: Crea variables para nombre_evento, dia, hora y lugar.
"""
nombre_evento = "Reunion familiar"
dia = "Martes"
hora = "7:00 am"
lugar = "Casa de la abuela"

print(f"Tengo una {nombre_evento}, el dia {dia} a las {hora} en la {lugar}")"""