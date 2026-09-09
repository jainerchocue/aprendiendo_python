# 📘 El uso de Funciones en Programación
# Las funciones son bloques de código reutilizables que nos permiten organizar mejor nuestros programas.

#============================================================================

# Ejercicio 1 — Función básica sin parámetros
def saludar():
    print("¡Hola! Bienvenido/a al mundo de la programación en Python")

saludar()

#============================================================================

# Ejercicio 2 — Función con un parámetro
def saludar_persona(nombre):
    print(f"¡Hola {nombre}!")

saludar_persona("María")
saludar_persona("Juan")

#============================================================================

# Ejercicio 3 — Función con un parámetro y retorno
def duplicar_numero(numero):
    resultado = numero * 2
    return resultado

resultado = duplicar_numero(5)
print(f"El doble de 5 es: {resultado}")

#============================================================================

# Ejercicio 4 — Función con un parámetro para verificar si es par
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(es_par(4))
print(es_par(7))

#============================================================================

# Ejercicio 5 — Función con un parámetro para calcular cuadrado
def calcular_cuadrado(numero):
    cuadrado = numero ** 2
    return cuadrado

resultado = calcular_cuadrado(3)
print(f"El cuadrado de 3 es: {resultado}")

#============================================================================

# Nuevos ejemplos sencillos

# Ejemplo 6: Función para sumar dos números
def sumar(numero1, numero2):
    return numero1 + numero2

print(sumar(3, 4))

# Ejemplo 7: Función para saludar con un mensaje
def mostrar_mensaje(mensaje):
    print(mensaje)

mostrar_mensaje("Hoy practicamos Python")

# Ejemplo 8: Función para calcular el precio total
def calcular_total(precio, cantidad):
    return precio * cantidad

total = calcular_total(2500, 3)
print(f"El total es: {total}")
