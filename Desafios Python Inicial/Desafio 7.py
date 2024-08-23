"""
7- La secuencia de Collatz de un número entero se construye de la siguiente forma:

● si el número es par, se lo divide por dos;

● si es impar, se le multiplica tres y se le suma uno;

● La sucesión termina al llegar a uno.

Desarrolle un programa que entregue la secuencia de Collatz de un número entero:
"""

numero = int(input("Ingrese un número entero: "))
secuencia = ""
while numero != 1:
    secuencia += str(numero) + " "
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
print(secuencia + "1")
