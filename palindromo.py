def main():
    word=str(input("Escribe una palabra:" ))
    result=palindromo2(word)
    if result is True:
        print('{} si es un palindromo'.format(word))
    else:
        print('{} no es un palindromo'.format(word))

def palindromo(word):
    reverse_letter=[]
    for letter in word:
        reverse_letter.insert(0,letter)
        reverse_word=''.join(reverse_letter)
    if reverse_word==word:
        return True
    return False
def palindromo2(word):
    reversed_word=word[::-1] #slice reordena la palabra, desde donde empiezo al final [:: -1] -1 pasos reversos
    if reversed_word==word:
        return True
    return False


if __name__=='__main__':
    main()
