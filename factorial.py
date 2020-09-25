def run():
    number=int(input("Ingrese el numero a calcular factorial: "))
    result=factorial(number)
    print(result)

def factorial(number):

    if number==0:
        return 1
    return number*factorial(number-1)



if __name__ =='__main__':
    run()