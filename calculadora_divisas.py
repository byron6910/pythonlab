def run():
    print('CALCULADORA DE  DIVISAS')
    print('Convierte calculadora de pesos mexicanos a colombianos')
    print('')

    amount=float(input('Ingresa la cantidad de pesos mexicanos a convertir: '))
    result=foreign_exchange_calculator(amount)
    print('La conversion es: ${} pesos mexicanos son ${} pesos colombianos'.format(amount,result))

def foreign_exchange_calculator(amount):
    mex_to_col=145.97
    return amount*mex_to_col



if __name__ == '__main__':
    run()