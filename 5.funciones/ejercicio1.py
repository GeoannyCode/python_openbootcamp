'''Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base 
como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.'''

import math

def area_triangulo(altura,base):
    return base*altura

def area_circulo(radio):
    return math.pi*(radio**2)

print("Triangulo: Altura")
altura = int(input())
print("Triangulo: Base")
base = int(input())

print("Círculo: radio")
radio = float(input())

print( "El área del triangulo es: "+ str(area_triangulo(altura,base)))
print("El área del círculo es: "+ str(area_circulo(radio)))

