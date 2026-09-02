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
