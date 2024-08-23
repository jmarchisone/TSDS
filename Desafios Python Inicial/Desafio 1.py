"""
1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso:
"""

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        str_numero = str(numero)
        inverso = ""
        for i in str_numero:
            inverso = i + inverso
        print(inverso)
        break
    except ValueError:
        print("Ingreso inválido.")
