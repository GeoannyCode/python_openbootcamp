"""Escribe una función que pueda decirte si un número (número entero) es primo o no."""

def es_primo(num):
    
    for i in range(2,num):
        if num%i == 0:
            return "No primo"
    return "Primo"
print("Ingrese el número a evaluar: ")

num = int(input())
print(es_primo(num))