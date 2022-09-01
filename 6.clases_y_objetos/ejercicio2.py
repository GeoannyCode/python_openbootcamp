"""

En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar 
sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

"""

def Evaluar(num):
    if num > 7:
        return "Aprobado"
    else:
        return "Reprobado"


class Alumno:

    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.resultado = Evaluar(nota)

    def __str__(self):
        return "Nombre: {}, Nota: {}, Estado: {}".format(self.nombre, self.nota, self.resultado)


alumno = Alumno("Diego", 8)
print(alumno)