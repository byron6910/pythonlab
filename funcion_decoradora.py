def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):# *args numero ilimitado de argumentos (4,5), **kwargs para pasar llaves (clave=valor) 
        #acciones adicionales que decoran
        print('Bienvenidos al calculo:')
        funcion_parametro(*args)
        #acciones adicionales que decoran
        print("hemos terminado el calculo")
    return funcion_interior

@funcion_decoradora
def suma(num1,num2):
    print(num1+num2)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

suma(7,5)
resta(3,2)
#if __name__=='__main__':
