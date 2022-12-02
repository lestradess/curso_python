class Vehiculo:
    color= "rojo"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 180
    cilindrada= 3000

ford = Coche()
print ("Color: ",ford.color)
print ("Ruedas: ",ford.ruedas)
print ("Puertas: ",ford.puertas)
print ("Velocidad: ",ford.velocidad)
print ("Cilindrada: ",ford.cilindrada)