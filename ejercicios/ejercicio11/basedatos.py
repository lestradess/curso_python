import sqlite3
# abrir conexión
db = sqlite3.connect("alumnos.bd")
# Abrir cursor
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS alumnos (
    id INT PRIMARI KEY AUTO_INCREMENT,
    nombre VARCHAR,
    apellido VARCHAR 
) ''')

alumnos = [
    (1, 'Pepe', 'Gotera'),
    (2, "Marco", "Antonio"),
    (3, "Federico", "Garcia"),
    (4, "Mercedes", "Milá"),
    (5, "Estefania", "Money"),
    (6, "Mauricio", "Calamar"),
    (7, "Guadalupe", "Martinez"),
    (8, "Ismael", "Serrano")]

cursor.executemany("INSERT INTO alumnos VALUES (?,?,?)", alumnos)
db.commit()
cursor.close()
db.close()

def pregunta_nombre ():
    db = sqlite3.connect("alumnos.bd")
    cursor = db.cursor()

    nombre = input("inserta nombre a buscar: ")

    row = cursor.execute(f"SELECT nombre FROM alumnos WHERE nombre='{nombre}'")

    data= row.fetchone()

    if data == None:
        return print("No existe el alumno.")
    else:
        row = cursor.execute(
            f"SELECT * FROM alumnos WHERE nombre='{nombre}'")
        data = row.fetchone()
        print(data)

    cursor.close()
    db.close()

pregunta_nombre()
