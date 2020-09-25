def main():
    #pass 
    # ##funcion que menciona que espera a la realizacion de la funcion.
    #u'niño' especifico unicode para que coja la ñ y acentos
    numero=int(input("Ingrese numero a calcular si es primo o no:"))
    result=es_primo(numero)
    if result==True:
        print("El numero ingresado es primo")
    else:
        print("no es primo")

def es_primo(numero):
    if numero <2:
        return False
    elif numero ==2: ##else if
        return True
    elif numero>2 and numero%2==0:
        return False
    else:
        for i in range (3,numero):
            if numero%i==0:
                return False
    return True




if __name__ == '__main__':
    main()
