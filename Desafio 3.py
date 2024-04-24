"""
3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
"""

numero = int(input("Ingrese un número entero: "))
primo = True
for i in range(2, numero):
    if numero % i == 0:
        primo = False
        break
if primo:
    print("Es primo.")
else:
    print(f"No es primo, {i} es divisor.")
