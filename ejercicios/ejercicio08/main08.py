archivo = open('texto.txt', 'w')
archivo.write('Hola archivo\n')
archivo.close()

archivo = open('texto.txt', 'a')
archivo.write('Texto 2')
# l1 = archivo.readline()
# l2 = archivo.readline()
archivo.close()

archivo = open('texto.txt', 'r')
print(f"línea1: {archivo.readline()}  linea2: {archivo.readline()} ")

archivo.close()
