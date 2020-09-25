class Lavadora:
    def __init__(self):
        pass
    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
    def _llenar_tanque_agua(self,temperatura):
        print('llenando el tanque de agua {temperatura}')
    
    def _anadir_jabon(self):
        print('agregando jabon')
    def _lavar(self):
        print('lavar la ropa')
    def _centrifugar(self):
        print('centrifugar la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()