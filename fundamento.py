# VARIABLES - ERROR COMÚN CON STRINGS
# ¿Te pasa esto? ¡Te explico cómo solucionarlo!

"""Error"""
"""
nombre = Juan
apellido = Campo
ciudad = Bogota

print(nombre)
print(apellido)
print(ciudad)"""



"""SOLUCIÓN: Agrega comillas a los strings"""
# ¡Los textos SIEMPRE van entre comillas!
"""
nombre = "Juan"
apellido = "Campo"
ciudad = "Bogota"

print(nombre)
print(apellido)
print(ciudad)"""

# ==================================================================
# ==================================================================


# FUNDAMENTOS DE PROGRAMACIÓN: ERRORES COMUNES AL IMPRIMIR

"""Error 1: Falta de comillas"""
# Para que Python entienda que algo es texto (string), DEBES usar comillas. 
# Sin ellas, el programa intentará buscar variables que no han sido creadas.
#print(Hola mundo)

"""Error 2: Comillas sin cerrar"""
# Las comillas funcionan como "llaves": si abres una para iniciar el texto, 
# obligatoriamente debes poner otra para indicar dónde termina.
#print("Hola mundo)

"""Error 3: Olvidar los paréntesis"""
# En Python 3, 'print' es una función. Esto significa que todo lo que 
# quieras mostrar en pantalla debe ir encerrado entre paréntesis ( ).
#print "Hola mundo"

#---------------------------------------------------#
# --------------- SOLUCIONES CORRECTAS --------------
"""
# Solución 1: Texto correctamente delimitado por comillas.
print("Hola mundo") 

# Solución 2: Estructura completa con comillas de apertura y cierre.
print("Hola mundo") 

# Solución 3: Uso correcto de la función con sus paréntesis obligatorios.
print("Hola mundo")"""

""""
# Calculadora de descuentos 1

# definimos una variable ej: precio

precio = 3500

# otra variable para  el descuento ej: descuento
descuento = 0.15

# variable para el resultado ej: resultado

resultado = precio-(precio*descuento)

#imprir el resultado con print()
print(resultado)

# ejecutar , resultado: 2975.0


# Es tu turno

Ahora intenta calcular el precio final de un televisor de $1,200,000 
aplicando un IVA del 19%. Escribe tu resultado en los comentarios"""


# Ejercicio 2: Propina en un restaurante
"""

#Definir una variable para la cuenta ej: cuenta
cuenta = 45000

# Definir una variable para la propina ej: propina

propina = 0.10 # El valor 0.10 equivale a 10%

# variable para calcular el resultado de la propina

resultado_propina = cuenta * propina

# variable para guardar el total

total = cuenta + resultado_propina

# imprimir

print(f"Total a pagar es: {total}\n")

# resultado: Total a pagar es: 49500.0"""




""" Conversion de segundos a minutos y horas."""
"""
#Definir una variable  para guardar el valor de segundo Ej: segundos == 1000

segundos = 1000 # Entrada

# variable para conversion de segundos a minutos

resultado_minutos = segundos / 60

# variable para conversion de  segundos a hora

resultado_hora = segundos/3600

# imprimir-> salidas
print(f"La conversion de segundos a minutos es: {resultado_minutos}")

print(f"La conversion de segundos a hora es: {resultado_hora}")

# resultados:

#La conversion de segundos a minutos es: 16.666666666666668
#La conversion de segundos a hora es: 0.2777777777777778"""




# CONDICIONALES
"""

# Define una variable con la edad de una persona (ejemplo: edad = 17).
# permitir que el usuario ingresa la edad

edad = int(input("ingrese su edad: "))

# Usa un condicional if para verificar si la edad es mayor o igual a 18.
if edad >= 18:
    # Si cumple, imprime: “Puedes entrar a la discoteca”.

    print("Puedes entrar a la discoteca 🥳 ")

else:
    print("No puedes entrar, eres menor de edad 🥲")
# Si no cumple, imprime: “No puedes entrar, eres menor de edad”."""

# Ejercicio 3
""" Verificar si un numero es par o impar.”"""
"""
num = int(input("ingrese un numero: "))

if num %2 ==0:
    print(num, "par")
else:
    print(num, "impar")


    def es_par(num):
        if num %2 ==0:
            return True
        else:
            return False

    def es_impar(num):
        if num %2 !=0:
            return True
        else:
            return False"""


# permutacion
"""
numero = int(input("Ingrese un numero: "))
lista = []
cont = 0

for i in range(numero+1):
    cont += 1
    resultado = cont*(cont-1)*(cont-2)
    print(resultado)
    print("valor cont",cont)
    lista.append(resultado)
print(lista)"""


# ejercicio 1
"""
numero = int(input("ingrese el valor: "))
lista = []
lista = [i for i in range(1, (numero*3 + 1))]

poscion = [lista[i + 1] for i in range(0 , numero*3,3)]

suma = sum(poscion)
print(suma)

"""




# fundamentos 











      