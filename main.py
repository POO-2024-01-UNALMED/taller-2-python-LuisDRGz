class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        cambio=["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in cambio:
            self.color=color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro=registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.Asiento[] = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        contador = 0
        for i in cantidadAsientos:
            if cantidadAsientos[i]!=null:
               contador+=1
        return contador

    def verificarIntegridad(self):
        if Asientos.registro==Motor.registro and Motor.registro==Auto.registro:
            return "Auto original"
        return "Las piezas no son originales"
