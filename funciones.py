#def sum (number1,number2):
  #  result=number1+number2
 #   return result
#print(sum(1,2))

import turtle

def main():
    windows=turtle.Screen()
    byron=turtle.Turtle()
    make_square(byron)
    turtle.mainloop()

def make_square(byron):
    length=int(input("Tamano de cuadrado: "))
    for i in range(4):
        make_line_turn(byron,length)

def make_line_turn(byron,length):
    
    byron.forward(length)
    byron.left(90)


if __name__ == '__main__': #funcion principal tipo void main java
    main()