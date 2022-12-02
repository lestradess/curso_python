class Dino:
    color = None
    nombre = None

    def __init__(self, color, nombre):
        self.nombre = nombre
        self.color = color


d = Dino("Rojo", "Dark")
print(d.color)
print(d.nombre)

