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
"""
#Crea tres variables con números.
#Calcula el promedio usando operaciones matemáticas.
#Imprime el resultado en un mensaje como:
#El promedio de ___, ___ y ___ es ___

valor1 = 10
valor2 = 8
valor3 = 9

promedio = (valor1 + valor2 + valor3) / 3

print(f"El promedio de {valor1}, {valor2} y {valor3} es: {promedio}")
"""

# =======================================================

# Ejercicio 5 — Área de un rectángulo
"""
# Crea dos variables base y altura.
# Calcula el área y muestra el resultado.

base = 10
altura = 20
area = base * altura

print(f"El area del rectangulo de base {base} y altura {altura} es {area}")
"""

# =======================================================

import math  # importamos math para poder utilziar el valro de pi que es  ~3.14

# Ejercicio 6: Área de un círculo
"""
# Crea una variable radio.
# Calcula el área usando la fórmula: área = pi * radio^2
# Muestra el resultado en un mensaje.


radio = 10
area = math.pi * radio**2

print(f"El area de un circulo de radio {radio} es {area}")
"""

# =======================================================

# Ejercicio 7: Área de un triángulo
"""
# Crea dos variables base y altura.
# Calcula el área usando la fórmula: (base * altura) / 2
# Muestra el resultado en un mensaje.

base = 5
altura = 10
area = (base*altura)/2
print(f"El area del triangulo de base {base} y altura {altura} es {area}")
"""

# =======================================================

# Ejercicio 8: Cálculo de descuento en una compra
"""
# Crea variables precio_original y porcentaje_descuento.
# Calcula el precio final aplicando la fórmula.
# Muestra el resultado en un mensaje.

precio_original = 10000 # precio colombiano
porcentaje_descuento = 10 # 10%

precio_final = precio_original -((precio_original*porcentaje_descuento)/100)

print(f"El precio  original era {precio_original}, con un descuento de {porcentaje_descuento}%, el preico fina es {precio_final}")
"""

# =======================================================

# Ejercicio 9 — Interés simple
"""
# Crea variables capital_inicial, tasa_interes y tiempo.
# Calcula el interés simple aplicando la fórmula: (capital_inicial * tasa_interes * tiempo) / 100
# Muestra el resultado en un mensaje.

capital_inicial = 10000
tasa_interes = 5
tiempo = 6 # anio

interes_simple =  (capital_inicial*tasa_interes*tiempo)/100
print(f"El interes generado  por un capital de {capital_inicial} a una tasa del {tasa_interes} % durante {tiempo} anios es { interes_simple}")
"""

# =======================================================

#Ejercicio 10 — Conversión de moneda
"""
# Crea una variable valor_cop (pesos colombianos).
# Crea una variable tasa_cambio (valor de 1 USD en COP).
# Calcula la conversión de COP a USD aplicando la fórmula: valor_cop / tasa_cambio
# Muestra el resultado en un mensaje.

valor_cop = 10000 # pesos colombianos
tasa_cambio = 3280
conversion = valor_cop / tasa_cambio
print(f"El valor de un usd 1 esta a {tasa_cambio} y la conversion de {valor_cop} colombianos a USD es de {conversion}")
"""
# =======================================================

#Ejercicio 11 — Conversión de tiempo
"""
# Crea una variable horas.
# Convierte esas horas a minutos y segundos.
# Muestra el resultado en un mensaje.

hora = 10 # 10 horas

minutos = hora * 60
segundos = hora * 3600

print(f"La conversion de {hora} horas a minutos es {minutos} y de hora a segundos es {segundos}")
"""

# =======================================================

# Ejercicio 12 — Cálculo de velocidad promedio
"""
# Crea variables distancia y tiempo.
# Calcula la velocidad promedio aplicando la fórmula: velocidad = distancia / tiempo
# Muestra el resultado en un mensaje.

distancia = 10
tiempo = 5

velocidad_promedio = distancia / tiempo
print(f"El resultado de la velocidad promedio es {velocidad_promedio}")
"""

# =======================================================

# Ejercicio 13 — Cálculo de salario con horas extras
"""
# Crea variables salario_base, horas_extras y valor_hora_extra.
# Calcula el salario total aplicando la fórmula: salario_total = salario_base + (horas_extras * valor_hora_extra)
# Muestra el resultado en un mensaje.

salario_base = 2500000 # valor en pesos colombianos
horas_extra = 5
valor_hora_extra = 10000 # pesos colombianos

salario_total = salario_base +(horas_extra * valor_hora_extra)

print(f"El salario base es de {salario_base}, y por las {horas_extra} horas extras, cada valor de hora extra tiene un valor de {valor_hora_extra}, la cual al final tiene que pagar {salario_total}")
"""



# =======================================================

#Ejercicio 14 — Promedio ponderado
"""
# Crea variables nota1, nota2, nota3 y sus respectivos pesos.
# Calcula el promedio ponderado aplicando la fórmula: promedio = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)
# Muestra el resultado en un mensaje.

# la nota tiene un rango de 0 a 5, 0=muy mal , 5 = muy bueno
# pesos 30% , 30% , 40%

nota1 = 3
peso1 = 0.30
nota2 = 4
peso2 = 0.30
nota3 = 5
peso3 = 0.40

promedio = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso3)

print(f"La nota final es {promedio}")
"""



# ==================================================================================
#  Ahora pedimos los datos al usuario para realizar las operaciones correspondientes.
# ==================================================================================

# Ejercicio 15 — Ley de Ohm (Física)

# La Ley de Ohm dice: V = I * R
# Donde:
# V = voltaje (en voltios)
# I = corriente (en amperios)
# R = resistencia (en ohmios)

# Pide al usuario ingresar corriente y resistencia.
# Calcula el voltaje aplicando la fórmula.
# Muestra el resultado en un mensaje.

corriente = float(input("Ingrese la corriente (A): "))
resistencia = float(input("Ingrese la resistencia (Ω): "))

voltaje = corriente * resistencia

print("El voltaje es ", voltaje ,"V")