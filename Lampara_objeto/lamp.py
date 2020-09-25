class Lamp:
   _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
   def __init__(self,_is_turn_on): #siempre se debe definir la propia instancia,en POO. init es el constructor.
      self._is_turn_on=_is_turn_on #inicializo la variable
   def turn_on(self):#self para acceder a la instancia
      self._is_turn_on=True
      self._display_image()
   def turn_off(self): #self es para poder seguir accediendo a esta instancia y las variables
      self._is_turn_on=False
      self._display_image()
   def _display_image(self):
      if self._is_turn_on:
         print(self._LAMPS[0])
      else:
         print(self._LAMPS[1])

def run():
   lamp=Lamp(_is_turn_on=False)
   while True:
      command=str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))
      if command=='p':
         lamp.turn_on()
      elif command=='a':
         lamp.turn_off()
      else:
         break

if __name__=='__main__':
   run()



