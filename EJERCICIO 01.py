from datetime import datetime

class Persona:
    def __init__(self):
        self.nombre= self.obtener_nombre()
        self.edad=self.obtener_edad()
        self.saldo=self.obtener_saldo()
        self.nacionalidad="peruana"
        
    def obtener_nombre(self):
        while True:
            try:
                nombre=input("Ingresar nombre:  ")
                if not nombre.isalpha():
                    raise ValueError("Error, el nombre debe contener letras")
                return nombre
            except ValueError as e:
                print(e)
                
    def obtener_edad(self):
        while True:
            try:
                edad = int(input("Ingresar edad:    "))
                if edad <=0:
                    raise ValueError("Error, la edad debe ser un numero entero positivo")
                return edad
            except ValueError as e:
                print(e)
    
    def obtener_saldo(self):
        while True:
            try: 
                saldo=float(input("Ingresar saldo:    "))
                return saldo
            except ValueError:
                print("el saldo deber ser un numero")
    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_actual = datetime.now()
        return fecha_actual.strftime("%Y-%m-%d %H:%M")

persona1=Persona()
print("Información de la primera persona:")
print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Saldo:", persona1.saldo)
print("Nacionalidad:", persona1.nacionalidad)

persona1.cumpleaños()
print("Después de un año, la edad de la primera persona es:", persona1.edad)

persona2 = Persona()
print("Información de la segunda persona:")
print("Nombre:", persona2.nombre)
print("Edad:", persona2.edad)
print("Saldo:", persona2.saldo)
print("Nacionalidad:", persona2.nacionalidad)

persona2.cumpleaños()
print("Después de un año, la edad de la segunda persona es:", persona2.edad)

fecha_registro = persona1.obtener_fecha_registro()
print("Fecha y hora de registro de la primera persona:", fecha_registro)


