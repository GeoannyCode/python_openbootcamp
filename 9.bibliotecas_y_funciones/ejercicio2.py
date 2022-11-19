'''
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de 
una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos
mediante reduce.
'''

import functools

def main(lista):
    print(lista)
    impares_lista = list(filter(lambda n : n%2 != 0, lista))
    print(impares_lista)
    suma_lista = functools.reduce(lambda a, b: a+b, impares_lista)
    print(f'La suma de todos los elementos es: {suma_lista}')
    

if __name__ == '__main__':
    numeros = [2,3,4,5,6,7,8]
    main(numeros)