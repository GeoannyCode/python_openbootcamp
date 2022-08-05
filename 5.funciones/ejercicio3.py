"""Escribe una función que pueda decirte si un año (número entero) es bisiesto o no."""

def bisiesto(year):
    if year%400 == 0:
        return "Es bisiesto"
    elif year%4 == 0 and year%100 != 0:
        return "Es bisiesto"
    return "No es bisiesto"

print("Ingrese el año:")
year = int(input())

print(bisiesto(year))
