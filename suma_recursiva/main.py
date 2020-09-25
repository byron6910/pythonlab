class Car:
    def __init__(self,color,placa,modelo):
        self.color=color
        self.placa=placa
        self.modelo=modelo

class Consecionario:
    def __init__(self):
        self._cars=[]
    def addCar(self,color,placa,modelo):
        car=Car(color,placa,modelo)
        self._cars.append(car)

    def printCar(self,car):
        print('El carro es de color {}, placa: {}, ,modelo:{}'.format(car.color,car.placa,car.modelo))

def run():
    carro=Car('rojo','pbcf9223','chevrolet')
    
if __name__ == '__main__':
    run()
