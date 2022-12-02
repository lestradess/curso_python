def bisiesto(numero):
    if numero % 4 == 0 and numero < 100:
        print("es bisiesto")
        if numero % 100 == 0 and numero % 400 == 0:
            print("es bisiesto")
    else:
        print("No es bisiesto")


respuesta = int(input("Dime un año: "))

bisiesto(respuesta)
