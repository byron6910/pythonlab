import random

def run():
    number_found=False
    limite=int(input("Ingrese hasta que numero es el limite: "))
    random_number=random.randint(0,limite)

    while not number_found:
        number=int(input("Intenta un numero: "))
        if number==random_number:
            print("Felicidades encontraste el numero")
            number_found=True
        elif number>number_found:
            print("Numero mas pequeno")
        else:
            print("el numero es mas grande")


if __name__=='__main__':
    run()