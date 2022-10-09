#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

def main():
    class Auto:
        
        def __init__(self, marca, modelo, anio, numero_puertas):
            self.marca = marca
            self.modelo = modelo
            self.anio = anio
            self.numero_puertas = numero_puertas

        def __str__(self):
            return f'''
            Marca: {self.marca}
            Modelo: {self.modelo}
            anio: {self.anio}
            numero_puertas: {self.numero_puertas}

            '''

    newAuto1 = Auto("Tesla","Model 3", 2019, 5)
    print(str(newAuto1))

    file = open('./tesla_model3.txt', 'w')
    file.write(str(newAuto1))
    
    file = open('tesla_model3.txt', 'r')
    tesla_model3 = file.read()
    print(tesla_model3)

if __name__ == "__main__":
    main()