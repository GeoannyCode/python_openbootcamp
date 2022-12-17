"""
En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que 
también será de tipo texto.

Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a 
la tabla.

Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.
"""

import sqlite3
conexion=sqlite3.connect("bd1.db")

try:
    conexion.execute(
    """
    create table Alumnos(
        id integer primary key autoincrement,
        nombre text,
        apellido text
    )
    """
    )
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla ya existe")


conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Diego", "Bracero"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Juan", "Alvan"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Carlos", "Montenegro"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Benito", "Huertas"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Maria", "de la Cruz"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Juanita", "Perez"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Daniel", "Martinez"))
conexion.execute("insert into Alumnos(nombre, apellido) values (?,?)", ("Lucy", "Encalada"))

conexion.commit()

name=input("Ingrese el nombre del estudiante:")
cursor=conexion.execute("select id,nombre,apellido from Alumnos where nombre=?", (name, ))
fila=cursor.fetchone()

if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()
