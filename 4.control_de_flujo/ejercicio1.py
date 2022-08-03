#Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

print("¿Cual es su edad?: ")

edad = input()

if int(edad) >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")