# Version: 0.2
# 📘 El uso de Tuplas en Python
# Las tuplas guardan varios valores en un orden fijo y no se pueden modificar.

# ==============================================================

# Nuevos ejemplos sencillos de tuplas

# Ejemplo 1: Crear una tupla y mostrarla
colores = ("rojo", "verde", "azul")
print(colores)

# Ejemplo 2: Acceder a elementos de una tupla
animales = ("perro", "gato", "conejo")
print(animales[0])
print(animales[1])

# Ejemplo 3: Recorrer una tupla
for animal in animales:
	print(f"Animal: {animal}")

# Ejemplo 4: Desempaquetar una tupla
nombre, edad, ciudad = ("Ana", 20, "Bogotá")
print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Ejemplo 5: Consultar cuántos elementos tiene una tupla
print(f"La tupla tiene {len(colores)} elementos")

# Ejemplo 6: Consultar el ultimo elemento
numeros = (10, 20, 30)
print(numeros[-1])

# Ejemplo 7: Consultar una posicion
meses = ("enero", "febrero", "marzo")
print(meses.index("febrero"))

# Ejemplo 8: Contar un valor
votos = ("si", "no", "si", "si")
print(votos.count("si"))

# Ejemplo 9: Revisar si un valor existe
animales = ("perro", "gato", "pez")
print("gato" in animales)

# Ejemplo 10: Crear una tupla de numeros
numeros = (2, 4, 6, 8)
print(numeros)

# Ejemplo 11: Sumar los valores de una tupla
precios = (1000, 2000, 3000)
print(sum(precios))

# Ejemplo 12: Recorrer una tupla de colores
colores = ("rojo", "verde", "azul")
for color in colores:
	print(color)

# Ejemplo 13: Tupla de datos de un producto
producto = ("cuaderno", 5000, 3)
print(f"Producto: {producto[0]}, precio: {producto[1]}")

# Ejemplo 14: Intercambiar valores con una tupla
primero = "A"
segundo = "B"
primero, segundo = segundo, primero
print(primero, segundo)

# Ejemplo 15: Tupla de un solo elemento
un_elemento = ("Python",)
print(un_elemento)
