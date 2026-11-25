# Version: 0.2
# 📘 El uso de Listas en Programación
# Las listas nos permiten almacenar múltiples valores en una sola variable.

#============================================================================

# Ejercicio 1 — Crear una lista simple y mostrarla
# Aquí creamos una lista con 3 frutas y la mostramos completa
frutas = ["manzana", "banana", "naranja"]
print(frutas)

#============================================================================

# Ejercicio 2 — Acceder a elementos de una lista por índice
# Las listas empiezan en índice 0, así que colores[0] es el primer elemento
colores = ["rojo", "verde", "azul"]
print(colores[0])  # Muestra: rojo
print(colores[1])  # Muestra: verde
print(colores[2])  # Muestra: azul

#============================================================================

# Ejercicio 3 — Agregar elementos a una lista
# El método append() agrega un elemento al final de la lista
numeros = [1, 2, 3]
numeros.append(4)  # Agregamos el número 4 al final
print(numeros)

#============================================================================

# Ejercicio 4 — Recorrer una lista con un ciclo
# El ciclo for nos permite recorrer cada elemento de la lista uno por uno
nombres = ["Ana", "Carlos", "María"]
for nombre in nombres:
    print(nombre)  # Imprime cada nombre individualmente

#============================================================================

# Ejercicio 5 — Obtener la longitud de una lista
# La función len() nos dice cuántos elementos tiene la lista
letras = ["a", "b", "c", "d", "e"]
cantidad = len(letras)
print(f"La lista tiene {cantidad} elementos")

#============================================================================

# Nuevos ejemplos sencillos

# ============================================================================

# Ejemplo 6: Cambiar un elemento de una lista
colores_favoritos = ["azul", "verde", "rojo"]
colores_favoritos[1] = "amarillo"
print(colores_favoritos)

# ============================================================================

# Ejemplo 7: Eliminar un elemento de una lista
animales = ["perro", "gato", "conejo"]
animales.remove("gato")
print(animales)

# ============================================================================

# Ejemplo 8: Ordenar una lista de números
calificaciones = [4, 2, 5, 3]
calificaciones.sort()
print(calificaciones)

# ============================================================================

# Ejemplo 9: Ordenar una lista al revés
numeros_ordenados = [1, 3, 2, 5]
numeros_ordenados.sort(reverse=True)
print(numeros_ordenados)

# ============================================================================

# Ejemplo 10: Agregar varios elementos
frutas_nuevas = ["manzana"]
frutas_nuevas.extend(["pera", "uva"])
print(frutas_nuevas)

# ============================================================================

# Ejemplo 11: Quitar el último elemento
colores = ["rojo", "verde", "azul"]
ultimo_color = colores.pop()
print(ultimo_color)
print(colores)

# ============================================================================

# Ejemplo 12: Revisar si un elemento existe
animales = ["perro", "gato", "pez"]
print("gato" in animales)

# ============================================================================

# Ejemplo 13: Contar un elemento
votos = ["si", "no", "si", "si"]
print(votos.count("si"))

# ============================================================================

# Ejemplo 14: Obtener la posición de un elemento
colores = ["rojo", "verde", "azul"]
print(colores.index("verde"))

# ============================================================================

# Ejemplo 15: Sumar números de una lista
precios = [1000, 2000, 3000]
print(sum(precios))

# ============================================================================

# Ejemplo 16: Copiar una lista
lista_original = [1, 2, 3]
lista_copia = lista_original.copy()
print(lista_copia)

# ============================================================================

# Ejemplo 17: Recorrer y mostrar precios
precios = [500, 1000, 1500]
for precio in precios:
    print(f"Precio: {precio}")

# ============================================================================

# Ejemplo 18: Crear una lista vacía y agregar datos
tareas = []
tareas.append("estudiar")
tareas.append("practicar")
print(tareas)
