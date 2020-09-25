def run():
    with open('byron.txt','w') as f: # with, manejador de contexto utilizado en pares por ejemplo #abrir archivo cerrar, para reducir consumo de memoria.
        for i in range(10):
            f.write(str(i))

def open_file2():
    counter=0
    with open('aleph.txt',encoding='utf-8') as f:
        for line in f:
            counter+=line.count('Beatriz')
    print('Beatriz se encuentra {} en el texto'.format(counter))

if __name__ =='__main__':
    #run()
    open_file2()
