"""
6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
triángulo rectángulo como el de más abajo con tantos renglones como indique el
usuario.
"""

renglones = int(input("Ingrese la cantidad de renglones: "))
triangulo = ""
for i in range(1, renglones + 1):
    triangulo += str(2 * i) + " "
    print(triangulo)
