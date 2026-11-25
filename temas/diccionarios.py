# Version: 0.2
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

# Ejercicio 5 — Mostrar claves y valores
# Los métodos keys() y values() muestran la información del diccionario
notas = {"matematicas": 85, "ingles": 90, "ciencias": 78}
print(notas.keys())
print(notas.values())

#============================================================================

# Nuevos ejemplos sencillos

# ============================================================================

# Ejemplo 6: Consultar los datos de un libro
libro = {"titulo": "Python fácil", "paginas": 120}
print(libro["titulo"])
print(libro["paginas"])

# ============================================================================

# Ejemplo 7: Eliminar una clave
celular = {"marca": "Samsung", "color": "negro", "precio": 500000}
del celular["color"]
print(celular)

# ============================================================================

# Ejemplo 8: Consultar otra clave
curso = {"nombre": "Python", "nivel": "inicial"}
print(curso["nivel"])

# ============================================================================

# Ejemplo 9: Consultar una clave con get()
usuario = {"nombre": "Laura", "edad": 22}
print(usuario.get("nombre"))

# ============================================================================

# Ejemplo 10: Agregar una ciudad
persona = {"nombre": "Carlos"}
persona["ciudad"] = "Pereira"
print(persona)

# ============================================================================

# Ejemplo 11: Modificar una edad
persona = {"nombre": "Ana", "edad": 20}
persona["edad"] = 21
print(persona)

# ============================================================================

# Ejemplo 12: Recorrer las claves
frutas = {"primera": "manzana", "segunda": "pera"}
for clave in frutas:
	print(clave)

# ============================================================================

# Ejemplo 13: Recorrer claves y valores
notas = {"matematicas": 4, "ingles": 5}
for materia, nota in notas.items():
	print(f"{materia}: {nota}")

# ============================================================================

# Ejemplo 14: Revisar si existe una clave
libro = {"titulo": "Python facil", "paginas": 100}
print("titulo" in libro)

# ============================================================================

# Ejemplo 15: Eliminar una clave con pop()
producto = {"nombre": "lapiz", "precio": 1000}
producto.pop("precio")
print(producto)

# ============================================================================

# Ejemplo 16: Contar elementos de un diccionario
colores = {"a": "rojo", "b": "azul", "c": "verde"}
print(len(colores))

# ============================================================================

# Ejemplo 17: Crear un diccionario vacío
contacto = {}
contacto["nombre"] = "Mario"
contacto["telefono"] = "3000000000"
print(contacto)

# ============================================================================

# Ejemplo 18: Guardar datos de una mascota
mascota = {"nombre": "Luna", "tipo": "perro", "edad": 3}
print(f"{mascota['nombre']} tiene {mascota['edad']} años")
