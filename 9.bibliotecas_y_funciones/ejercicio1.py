# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


countries = input('Ingrese los paises separados por comas > ')
#String a lista
countries = countries.split(',')
#Eliminar espacios
countries = list(map(lambda x: x.strip(), countries))
#Ordenado Alfabeticamente
countries.sort()
#Eliminar repetidos
countries = list(set(countries))
print(countries)
