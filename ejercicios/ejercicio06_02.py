class Alumno:

    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostar_datos(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def notas(self):
        if self.nota < 5:
            print("El alumno ha suspendido")
        else:
            print("El alumno ha aprobado")

alumno = Alumno()
alumno.datos("Jose",8)
alumno.mostar_datos()
alumno.notas()
