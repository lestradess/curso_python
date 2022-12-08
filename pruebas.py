import sqlite3
# abrir conexión
db = sqlite3.connect("borrar.db")
# Abrir cursor
cursor = db.cursor()
rows = cursor.execute("INSERT INTO users VALUES ('2','lolo','cdsf','miclave')")
db.commit()

cursor.close()
db.close()
