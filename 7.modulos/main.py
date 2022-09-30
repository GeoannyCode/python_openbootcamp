"""
En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: 
sumar, restar, multiplicar y dividir. Este módulo lo importaréis a un archivo python y llamaréis a las 
funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

import operaciones.calculadora as op

def main():
        num1 = int(input("Ingresa num1: "))
        num2 = int(input("Ingresa num2: "))
        
        suma = op.sumar(num1,num2)
        res = op.restar(num1, num2)
        por = op.mutiplicar(num1, num2)
        div = op.dividir(num1,num2)

        print(f'{num1} + {num2} = {suma}')
        print(f'{num1} - {num2} = {res}')
        print(f'{num1} * {num2} = {por}')
        print(f'{num1} / {num2} = {div}')

if __name__ == "__main__":
    main()