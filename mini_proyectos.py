# Version: 0.2
# ✨ ¡Hola! Por el momento este archivo está vacío, ya que vamos paso a paso.
# 
# Te invito a revisar los otros archivos del repositorio donde ya voy subiendo 
# varios códigos de ejemplo para que puedas ir practicando y estudiando.
# 
# Si te gusta este material, no olvides darme un "Like" para apoyar el proyecto:
# ⭐ Aquí en GitHub: Haz clic en el botón de la estrellita (Star).
# ❤️ En TikTok: Regálame un corazoncito en los videos.
# 
# ¡Muchas gracias por aprender tecnología conmigo y ser parte de esta comunidad! 🙌

# ==============================================================

# Nuevos mini proyectos sencillos

# Proyecto 1: Presentación personal
nombre = "Jainer"
edad = 25
ciudad = "Bogota"

print(f"Mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.")

# Proyecto 2: Calculadora de una compra
producto = "Cuaderno"
precio = 5000
cantidad = 2
total = precio * cantidad

print(f"Producto: {producto}")
print(f"Total a pagar: {total}")

# Proyecto 3: Convertidor de temperatura
celsius = 25
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} grados Celsius son {fahrenheit} Fahrenheit.")

# Proyecto 4: Calculadora de promedio
nota1 = 4
nota2 = 5
nota3 = 3
promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio es {promedio}.")

# Proyecto 5: Lista de compras
compras = ["pan", "leche", "huevos"]
print("Lista de compras:")
for compra in compras:
	print(compra)

# Proyecto 6: Verificador de edad
edad = 17
if edad >= 18:
	print("La persona es mayor de edad.")
else:
	print("La persona es menor de edad.")

# Proyecto 7: Conversor de tiempo
horas = 2
minutos = horas * 60
print(f"{horas} horas son {minutos} minutos.")

# Proyecto 8: Registro de un contacto
contacto = {"nombre": "Laura", "telefono": "3000000000"}
print(f"Contacto: {contacto['nombre']} - {contacto['telefono']}")

# Proyecto 9: Contador de ahorro
ahorro_inicial = 10000
ahorro_semana = 5000
ahorro_total = ahorro_inicial + ahorro_semana
print(f"El ahorro total es {ahorro_total} pesos.")

# Proyecto 10: Tabla de multiplicar
numero = 4
for multiplicador in range(1, 6):
	print(f"{numero} x {multiplicador} = {numero * multiplicador}")

# Proyecto 11: Inventario sencillo
inventario = {"cuadernos": 5, "lapices": 10}
print(f"Cuadernos disponibles: {inventario['cuadernos']}")

# Proyecto 12: Mensaje personalizado
nombre_usuario = "Sofia"
mensaje = f"Hola {nombre_usuario}, sigue practicando Python."
print(mensaje)
