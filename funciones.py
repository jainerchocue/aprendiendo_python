# Version: 0.2
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

# Ejemplo 9: Funcion para restar dos numeros
def restar(numero1, numero2):
    return numero1 - numero2

print(restar(10, 3))

# Ejemplo 10: Funcion para multiplicar dos numeros
def multiplicar(numero1, numero2):
    return numero1 * numero2

print(multiplicar(4, 5))

# Ejemplo 11: Funcion para convertir minutos a segundos
def convertir_a_segundos(minutos):
    return minutos * 60

print(convertir_a_segundos(2))

# Ejemplo 12: Funcion para verificar si una persona es adulta
def es_adulto(edad):
    return edad >= 18

print(es_adulto(20))

# Ejemplo 13: Funcion para obtener el mayor de dos numeros
def mayor_de_dos(numero1, numero2):
    if numero1 > numero2:
        return numero1
    return numero2

print(mayor_de_dos(8, 5))

# Ejemplo 14: Funcion para calcular el promedio
def calcular_promedio(nota1, nota2):
    return (nota1 + nota2) / 2

print(calcular_promedio(4, 5))

# Ejemplo 15: Funcion con un valor por defecto
def saludar_con_nombre(nombre="estudiante"):
    print(f"Hola, {nombre}")

saludar_con_nombre()
saludar_con_nombre("Sofia")

# Ejemplo 16: Funcion para calcular el area de un rectangulo
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5, 3))

# Ejemplo 17: Funcion para convertir kilometros a metros
def convertir_a_metros(kilometros):
    return kilometros * 1000

print(convertir_a_metros(2))

# Ejemplo 18: Funcion para contar letras
def contar_letras(palabra):
    return len(palabra)

print(contar_letras("Python"))
