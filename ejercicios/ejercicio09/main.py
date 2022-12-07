


paises = input("introduce una lista de paises separados por comas ").split(",")
#paises = ["España", "Francia", "Grecia", "Alemania", "España", "4je","45",]

sinRepes = sorted(set(paises))

print(",".join(sinRepes))
