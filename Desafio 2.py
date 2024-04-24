"""
2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
"""

hora_actual = int(input("Ingrese la hora actual: "))
horas_agregadas = int(input("Cuantas horas se agregaran? "))
print(
    f"En {horas_agregadas} horas, el reloj marcará las {(hora_actual + horas_agregadas) % 12} horas."
)
