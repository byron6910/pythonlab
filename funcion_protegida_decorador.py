# -*- coding: utf-8 -*-
def protected(func): # funcion con parametro una funcion, a eso se denomina decorador
    def wrapper(password):
        if password=='platzi':
            return func()
        else:
            print("contrasena incorrecta")
    return wrapper

@protected

def protected_func():
    print('tu contrasena correcta:')


if __name__=='__main__':
    password=str(input("Ingresa tu password:"))
    protected_func(password)

