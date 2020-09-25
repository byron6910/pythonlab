class Coordenada:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distancia(self,otra_coordenada):
        x_diff=(self.x-otra_coordenada.x)**2
        y_diff=(self.y-otra_coordenada.y)**2
        return(x_diff+y_diff)**0.5
if __name__=='__main__':
    coordenada1=Coordenada(3,30)
    coordenada2=Coordenada(4,8)
    #print(coordenada1.distancia(coordenada2))

    print(isinstance(coordenada1,Coordenada))# permite definir si alguna de las instancias de Coordenada es Coordenada1

