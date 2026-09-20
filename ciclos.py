# Version: 0.2
# Loops Topic
"""
# Exercise 1 — Print numbers from 1 to 10
# Problem:
# Create a program that prints the numbers from 1 to 10.
# - Use a "for" loop.
# - Each number should appear on a new line.

for i in range(1, 11):
    print(i)
"""
#==============================================================

"""
# Exercise 2 — Print numbers backwards

# Problem:
# Create a program that prints the numbers from 10 down to 1.
# - Use a "for" loop.
# - Each number should appear on a new line.

for i in range(10,0, -1):
    print(i)
"""
#==========================================================
"""
# Exercise 3 — Multiples of 3

# Problem:
# Create a program that prints the multiples of 3 from 3 up to 30.
# - Use a "for" loop.
# - Each multiple should appear on a new line.

for i in range(3,33,3):
    print(i)

"""
#==========================================================

"""
# Exercise 4 — Squares of numbers

# Problem:
# Create a program that prints the squares of the numbers from 1 to 10.
# - Use a "for" loop.
# - Each result should appear on a new line.

for i in range(1,11):
    print(i**2)
"""

#==========================================================

"""
# Exercise 5 — Cubes of numbers

# Problem:
# Create a program that prints the cubes of the numbers from 1 to 10.
# - Use a "for" loop.
# - Each result should appear on a new line.

for i in range(1,11):
    print(i**3)
"""

#==========================================================

"""
# Exercise 6 — Multiplication table

# Problem:
# Create a program that prints the multiplication table of 5 (from 1×5 up to 10×5).
# - Use a "for" loop.
# - Each result should appear on a new line in the format: "5 x n = result".

valor = 5
for i in range(1,11,1):
    multiplicacion = i * valor
    print(f"{i}*{valor} = {multiplicacion}")

"""

#==========================================================

"""
# Exercise 7 — Full multiplication table

# Problem:
# Create a program that prints the multiplication tables from 1 to 10.
# - Use a "for" loop inside another "for" loop (nested loops).
# - Each table should show results from 1×n up to 10×n.
# - Separate each table with a blank line for clarity.

for i in range(1, 11):
    for j in range(1,11):
        resul = i * j
        
        print(f"{i}*{j} = {resul}")
    print("................")
"""

#==========================================================

"""
# Exercise 8 — Triangle pattern with stars

# Problem:
# Create a program that prints a triangle made of stars (*).
# - Use a "for" loop.
# - The first line should have 1 star, the second line 2 stars, and so on.
# - Continue until the fifth line, which should have 5 stars.

for i in range(1,6):
    print("*"*i)
"""


#==========================================================

# Exercise 9 — Inverted triangle of stars

"""
# Problem:
# Create a program that prints an inverted triangle made of stars (*).
# - Use a "for" loop.
# - The first line should have 5 stars, the second line 4 stars, and so on.
# - Continue until the last line, which should have 1 star.

for i in range(5,0,-1):
    print("*"*i)"""

#==========================================================


# Exercise 10 — Pyramid of stars (centered)

# Problem:
# Create a program that prints a centered pyramid made of stars (*).
# - Use a "for" loop.
# - The pyramid should have 5 levels.
# - Each level should be centered by adding spaces before the stars.

for i in range(1,6):
    spaces = " "*(5 - i)
    starts = "*" * (2*i -1)
    print(spaces + starts)

# Exercise 11 - Print even numbers
for numero in range(2, 11, 2):
    print(numero)

# Exercise 12 - Add numbers from 1 to 5
total = 0
for numero in range(1, 6):
    total = total + numero
print(f"The total is {total}")

# Exercise 13 - Print the letters of a word
palabra = "Python"
for letra in palabra:
    print(letra)

# Exercise 14 - Count from 5 to 10
for numero in range(5, 11):
    print(numero)

# Exercise 15 - Print a list of colors
colores = ["red", "green", "blue"]
for color in colores:
    print(color)

# Exercise 16 - Count vowels in a word
palabra = "banana"
contador = 0
for letra in palabra:
    if letra in "aeiou":
        contador = contador + 1
print(f"The word has {contador} vowels")

# Exercise 17 - Print multiples of 2
for numero in range(2, 13, 2):
    print(f"2 x {numero // 2} = {numero}")

# Exercise 18 - Show a small rectangle
for fila in range(3):
    print("***")

# Exercise 19 - Count down from 5
for numero in range(5, 0, -1):
    print(numero)

# Exercise 20 - Find the largest number in a list
numeros = [4, 8, 2, 6]
mayor = numeros[0]
for numero in numeros:
    if numero > mayor:
        mayor = numero
print(f"The largest number is {mayor}")