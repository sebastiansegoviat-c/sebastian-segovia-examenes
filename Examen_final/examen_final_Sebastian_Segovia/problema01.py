"""
1. Escriba un programa donde tendrá los siguientes requisitos

"""

class Persona:
    def __init__(self, nombre="", edad=0, nacionalidad="peruana", saldo=250):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.saldo = saldo
    def actualizar_nombre(self):
        self.nombre = input("Actualice su nombre: ")
    def actualizar_edad(self):
        while True:
            try:
                self.edad = int(input("Actualice su edad: "))
                if self.edad <= 0:
                    raise ValueError
                else:
                    print(f"Su edad es: {self.edad}")
                    break
            except ValueError:
                print("El edad no es valida")

    def cumplir_años(self):
        self.edad = self.edad + 1
        print(f"Su edad actualizada es: {self.edad}")
    def mostrar_saldo(self, saldo):
        self.saldo = int("Ingresa su saldo: ")
        print(f"Su saldo es: {self.saldo}")
    def transferir(self, destino):
        monto = int(input("Transferir la cantidad de: "))
        if self.saldo < monto:
            print("Saldo insuficiente")
        else:
            self.saldo -= monto
            destino.saldo += monto
            print(f"Se transfirió {monto} a {destino.nombre}")


class Empleado(Persona):
    def __init__(self, nombre="", edad=0, nacionalidad="peruana", saldo=0, sueldo=0):
        super().__init__(nombre, edad, nacionalidad, saldo)
        self.sueldo = float(sueldo)

    def aumento_sueldo(self, porcentaje=0.3):
        self.sueldo = self.sueldo + (self.sueldo * porcentaje)
    def prediccion(self):
        while True:
            try:
                edad_param = int(input("Elija el año de la predicción: "))
                if edad_param < self.edad:
                    raise ValueError
                else:
                    años = edad_param - self.edad
                    años_actual = 2025
                    año_objetivo = años_actual + años
                    print(f"En el año {año_objetivo} tendra {edad_param}")
                    break
            except ValueError:
                print("No es posible realizar la operación")


persona_1 = Empleado()
persona_2 = Empleado()

print("\n////Persona_1: ")
persona_1.actualizar_nombre()
print("----------------------------------------------------")
persona_1.actualizar_edad()
print("----------------------------------------------------")
persona_1.cumplir_años()
print("----------------------------------------------------")
persona_1.aumento_sueldo()
print("----------------------------------------------------")
persona_1.prediccion()
print("----------------------------------------------------")

print("\n////Persona_2: ")
persona_2.actualizar_nombre()
print("----------------------------------------------------")
persona_2.actualizar_edad()
print("----------------------------------------------------")
persona_2.cumplir_años()
print("----------------------------------------------------")
persona_2.aumento_sueldo()
print("----------------------------------------------------")
persona_2.prediccion()


print("\n////Transferencias:")

persona_1.transferir(persona_2)
print("----------------------------------------------------")
persona_2.transferir(persona_1)
print("----------------------------------------------------")
persona_1.mostrar_saldo()
print("----------------------------------------------------")
persona_2.mostrar_saldo()
print("----------------------------------------------------")