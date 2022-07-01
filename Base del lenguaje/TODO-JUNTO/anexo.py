class FuckException(Exception):
    pass


class Punto:
    def es_numero(valor):
        """ Indica si un valor es numérico o no. """
        return isinstance(valor, (int, float, complex))

    def __init__(self, x=0, y=0):
        """ Constructor de Punto, x e y deben ser numéricos,
    de no ser así, se levanta una excepción TypeError """
        if Punto.es_numero(x) and Punto.es_numero(y):
            self.x = x
            self.y = y
        else:
            print('Disparo fuck Exception')
            raise FuckException
            #esta linea no se ejecutaria:
            raise TypeError("x e y deben ser valores numéricos")

    def mostrar(self):
        print(self.y)
        print(self.y)

    def __str__(self):
        return (str(self.x) + ' , ' + str(self.y))


# def prueba(self, z):
#   print(es_numero(z))
#por que no reconoce es_numero sin poner punto antes?

    def __add__(self, otro):
        aa = self.x + otro.x
        bb = self.y + otro.y
        nuevo = Punto(aa, bb)
        return nuevo
