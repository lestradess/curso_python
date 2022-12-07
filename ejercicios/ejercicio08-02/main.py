import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"marca: {self.marca} Modelo: {self.modelo}"


coche = Vehiculo("Seat", "Panda")
print(coche)
objeto = open("vehiculo.bin", "wb")
pickle.dump(coche, objeto)
objeto.close()

objeto2 = open("vehiculo.bin", "rb")
cocheCargado = pickle.load(objeto2)
print(f"Coche Cargado: {cocheCargado}")
objeto.close()
