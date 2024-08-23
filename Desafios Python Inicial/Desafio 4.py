"""
4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.
Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
"""

tiempo_total = 0
while True:
    tiempo = int(input("Ingrese los minutos del tramo, o 0 para finalizar: "))
    tiempo_total += tiempo
    if tiempo == 0:
        break
print(f"El tiempo total es de {tiempo_total // 60}:{tiempo_total % 60} hs")
