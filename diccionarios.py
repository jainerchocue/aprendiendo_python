# 📘 El uso de Diccionarios en Programación
# Los diccionarios almacenan datos en pares clave-valor, como un diccionario real.

#============================================================================

# Ejercicio 1 — Crear un diccionario simple y mostrarlo
# Aquí creamos un diccionario con información de una persona
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}
print(persona)

#============================================================================

# Ejercicio 2 — Acceder a valores usando claves
# Usamos la clave entre corchetes para obtener el valor correspondiente
producto = {"nombre": "Laptop", "precio": 800, "stock": 10}
print(producto["nombre"])   # Muestra: Laptop
print(producto["precio"])   # Muestra: 800
print(producto["stock"])    # Muestra: 10

#============================================================================

# Ejercicio 3 — Agregar un nuevo par clave-valor
# Simplemente asignamos un valor a una nueva clave
estudiante = {"nombre": "Ana", "grado": "10"}
estudiante["edad"] = 16  # Agregamos la edad
print(estudiante)

#============================================================================

# Ejercicio 4 — Modificar un valor existente
# Podemos cambiar el valor de una clave existente
configuracion = {"tema": "oscuro", "idioma": "español"}
configuracion["tema"] = "claro"  # Cambiamos el tema
print(configuracion)

#============================================================================

# Ejercicio 5 — Recorrer un diccionario
# El ciclo for nos permite recorrer las claves del diccionario
notas = {"matematicas": 85, "ingles": 90, "ciencias": 78}
for materia in notas:
    print(f"{materia}: {notas[materia]}")
