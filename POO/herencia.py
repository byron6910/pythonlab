class Rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura

class Cuadrado(Rectangulo): ##la clase cuadrado, extiende de rectangulo
    def __init__(self,lado):
        super().__init__(lado,lado)#permite obtener una referencia de la super clase Rectangulo

if __name__=='__main__':
    rectangulo=Rectangulo(3,4)
    print(rectangulo.area())

    cuadrado=Cuadrado(lado=5)
    print(cuadrado.area())