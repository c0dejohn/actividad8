"""
    autor: john manyoma

    Jugando con operaciones básicas

    """


def suma(a, b):
    print(a+b)


def resta(a, b):
    print((a-b))


def multiplicacion(a, b):
    print(a*b)


def division(a, b):
    print(a/b)


a = float(input("ingrese el primer número: "))
b = float(input("ingrese el segundo número: "))


print("""
     Elija la operación deseada
        
         +) Suma
         -) Resta
         *) Multiplicación
         /) División
        
      """)
operacion = input("ingrese símbolo de la operación:")

if operacion == '+':
    suma(a, b)
elif operacion == '-':
    resta(a, b)
elif operacion == '*':
    multiplicacion(a, b)
elif operacion == '/':
    division(a, b)
else:
    print("valor no válido")
