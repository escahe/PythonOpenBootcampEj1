class Vehiculo:
    color,ruedas,puertas = None,None,None
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad, cilindrada = None,None
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        super().__init__(color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche = Coche('rojo',4,4,200,2000)
print(
    f'\nDetalles del coche:\nColor: {coche.color}\nRuedas: {coche.ruedas}',
    f'\nPuertas: {coche.puertas}\nVelocidad: {coche.velocidad}kmph\nCilindrada: {coche.cilindrada}cc'
)