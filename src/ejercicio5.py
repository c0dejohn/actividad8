"""
      Jugando con operaciones básicas

 """


def factorial(numero):
    return 1 if (numero == 1 or numero == 0) else numero * factorial((numero - 1))


numero = int(input("ingresar un número : "))

print("el factorial es : ", factorial(numero))
