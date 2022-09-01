"""En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
Color
Ruedas
Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
Velocidad
Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola."""

class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        return "Color: {}, Ruedas: {}, Puertas: {}".format( self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):

    def __init__(self,color,ruedas,puertas, velocidad, cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return "Color: {}, Ruedas: {}, Puertas: {}, Velocidad: {}, Clilindrada: {}".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)
        

coche = Coche("negro", 4, 5, 120, 10 )

print(coche)


