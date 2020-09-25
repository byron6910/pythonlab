def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False

# Reemplazar el operador / por el (//)	
    mid = (low + high) // 2
    print(mid)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)

def run():
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

# Reemplazar el Keyword raw_input por (INPUT)
    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número SÍ está en la lista.')
    else:
        print('El número NO está en la lista.')

if __name__ == '__main__':
    run()