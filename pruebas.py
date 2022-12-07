# open("directorio", "permiso")
# Permisos:
# r: lectura    "Solo lectura"
# a: append     "Añadir datos a un fichero al final "
# w: escritura  "Sobreescribir todo el fichero"
# x: create     "crea el fichero si no exite"

# t: texto
# b: binary
# +: plus
# Los permios se pueden combinar: rw
import pickle  # se necesita para serializar y deserializar


class Estado:
    player = "players"
    status = "status"
    life = 12
    armor = True


# Con wb creamos, si no existe y escribimos un fichero binario borrando el anterior
f = open("game.bin", "wb")
e = Estado()
#pickle.dump archivo, fichero)
pickle.load(f)
f.close()
