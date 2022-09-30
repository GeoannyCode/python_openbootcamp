"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación 
para calcular el tiempo que queda de trabajo.
"""
import time

def main():
    tiempo = 'time():', time.ctime(time.time()), '\nlocaltime():', time.localtime()

    hora_actual = tiempo[3][3]

    if hora_actual >= 19:
        print("Hora de ir a casa")
    else:
        print(f'Faltan {19 - hora_actual} para ir a casa')


if __name__ == "__main__":
    main()