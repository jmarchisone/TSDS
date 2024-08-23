"""
8- Este problema apareció en el certamen recuperativo 1 del segundo semestre de 2011
en el campus Vitacura.
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.
"""

productos = {"A": 270, "B": 340, "C": 390}
compra = str(input("Ingrese el producto a comprar: "))
monedas = int(input("Ingrese monedas, o ingrese 0 para finalizar: "))
saldo = monedas
while monedas != 0:
    monedas = int(input("Ingrese monedas, o ingrese 0 para finalizar: "))
    saldo += monedas
vuelto = saldo - productos[compra.upper()]
print(
    f"Su vuelto es {vuelto}: {vuelto // 100} monedas de 100, {vuelto % 100 // 50} monedas de 50, y {vuelto % 100 % 50 // 10} monedas de 10."
)
