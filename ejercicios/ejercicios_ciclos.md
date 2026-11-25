# 📘 Ejercicios de Ciclos

Bienvenido/a a los ejercicios de ciclos. Aquí encontrarás desafíos para practicar la repetición de tareas con `for` y `range()` en Python.

## 📝 Instrucciones:

1. Lee cada enunciado cuidadosamente
2. Intenta resolver el ejercicio por tu cuenta
3. Si necesitas ayuda, revisa el archivo `temas/ciclos.py` donde encontrarás ejemplos similares
4. Practica, practica y practica ¡Esa es la clave del aprendizaje!

---

## Ejercicio 1 — Contar del 1 al 10

**Enunciado:**
Usa un ciclo `for` con `range()` para imprimir los números del `1` al `10`, uno por línea.

**Objetivo:**
- Entender cómo funciona `range(inicio, fin)`
- Recordar que el límite superior no se incluye

---

## Ejercicio 2 — Cuenta regresiva

**Enunciado:**
Imprime los números del `10` al `1` en orden descendente usando un ciclo `for`.

**Objetivo:**
- Usar el tercer parámetro (paso negativo) en `range()`
- Controlar el sentido del conteo

---

## Ejercicio 3 — Múltiplos de 3

**Enunciado:**
Muestra todos los múltiplos de `3` desde el `3` hasta el `30` usando un ciclo `for`.

**Objetivo:**
- Utilizar incrementos personalizados en `range()`
- Evitar cálculos innecesarios cuando el paso resuelve el problema

---

## Ejercicio 4 — Tabla de multiplicar

**Enunciado:**
Pide o define un número entero e imprime su tabla de multiplicar del `1` al `10` con el formato `"5 x 1 = 5"`.

**Objetivo:**
- Combinar la variable del ciclo con operaciones dentro del bucle
- Formatear la salida con f-strings

---

## Ejercicio 5 — Suma acumulada

**Enunciado:**
Calcula la suma de todos los números del `1` al `20` usando una variable acumuladora dentro de un ciclo `for`.

**Objetivo:**
- Aprender el patrón de variable acumuladora (`total = total + numero`)
- Mostrar el resultado final fuera del ciclo

---

## Ejercicio 6 — Recorrer letras de una palabra

**Enunciado:**
Guarda una palabra en una variable e imprime cada una de sus letras en una línea distinta usando `for`.

**Objetivo:**
- Entender que las cadenas de texto también se pueden recorrer
- Iterar directamente sobre elementos sin usar índices

---

## Ejercicio 7 — Contar vocales

**Enunciado:**
Dada una palabra, recorre sus letras y cuenta cuántas vocales tiene en total.

**Objetivo:**
- Combinar un ciclo `for` con un condicional `if`
- Usar una variable contadora

---

## Ejercicio 8 — Suma de números pares

**Enunciado:**
Calcula la suma de todos los números pares entre `1` y `20` verificando cada número dentro del ciclo.

**Objetivo:**
- Integrar el operador módulo `%` dentro de un bucle
- Filtrar qué valores se acumulan

---

## Ejercicio 9 — Triángulo de asteriscos

**Enunciado:**
Imprime un triángulo creciente de `5` filas usando `*`, donde la fila 1 tiene un asterisco y la fila 5 tiene cinco.

**Objetivo:**
- Multiplicar cadenas de texto por un número (`"*" * i`)
- Visualizar cómo cambia la variable del ciclo en cada vuelta

---

## Ejercicio 10 — Encontrar el número mayor

**Enunciado:**
Dada una lista de números (por ejemplo `[12, 45, 7, 89, 23]`), recórrela con un ciclo `for` y encuentra cuál es el número mayor sin usar `max()`.

**Objetivo:**
- Aplicar lógica de comparación paso a paso dentro de un ciclo
- Mantener una variable con el mejor resultado encontrado hasta el momento

---

## 💡 Tips para resolver:

- Recuerda indentar con 4 espacios el bloque que va dentro del `for`
- `range(1, 11)` genera números del 1 al 10
- Inicializa contadores y acumuladores en `0` antes de empezar el ciclo
- Si quieres mostrar un total final, pon el `print()` fuera del ciclo (sin indentación)

## 🌟 ¡Mucha suerte con tus ejercicios!

Recuerda: los ciclos automatizan tareas repetitivas y son esenciales en todo programa. ¡Sigue practicando!
