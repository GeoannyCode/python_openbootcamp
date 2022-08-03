#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

from ast import Num


print("numero inicial: ")
num_inicial = int(input())

print("numero final")
num_final = int(input())

lista_impares = []

while num_inicial <= num_final:
    if num_inicial % 2 != 0:
        lista_impares.append(num_inicial)
    num_inicial += 1
print(lista_impares)
