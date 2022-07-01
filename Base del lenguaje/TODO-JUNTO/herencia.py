class vehiculo:
    nombre = 'No tengo nombre aun'
    ruedas = 0

    def __init__(self, nombre, ruedas):
        self.nombre = nombre
        self.ruedas = ruedas

    def __str__(self):
        return 'Esta es mi __str__ descripcion textual: ' + self.nombre

    def definite(self):
        print('soy un vehiculo')

    def __add__(self, otro):
        total = self.ruedas + otro.ruedas
        return total

    def categorias(self):
        print(' Aereo Maritimo Terrestre')


class avion(vehiculo):
    def definite(self):
        super().definite()
        print('soy un avion')
        print('Me llamo : ' + self.nombre)


class auto(vehiculo):
    pass
