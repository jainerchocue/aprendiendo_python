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
