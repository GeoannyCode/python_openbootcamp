#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis 
# dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

open("./archivo.txt", "w")
texto = open("./archivo.txt", "w")

texto.write("Hola mundo")

texto.close()