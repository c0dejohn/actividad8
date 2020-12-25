"""
author: john manyoma
@c0dejohn

Métodos para hacar cálculos con figuras

"""
PI = 3.1416

# definición de funciones


def circulo(r):
    area = float(PI*pow(r, 2))
    resultado = "{:.2f}".format(float(area))
    return print("el valor de área es : ", resultado, "cm2")


def cuadrado(l):
    area = pow(l, 2)
    return print("el área del cuadrado es :", "{:.2f}".format(float(area)), "cm2")


def triangulo(b, h):
    area = b*(h/2)
    return print("el área del triangulo es :", "{:.2f}".format(float(area)), "cm2")


# menú de opciones

print("""
       Figuras disponibles para calcular el área:

        1) Círculo
        2) Cuadrado
        3) Triángulo

      """)
figura = int(input('\nEliga número de la figura: '))

# validación de opción elegida

if figura == 1:
    r = float(input("ingrese valor de radio: "))
    circulo(r)

elif figura == 2:
    l = float(input("ingrese valor para lado: "))
    cuadrado(l)

elif figura == 3:
    b = float(input("ingrese valor para base: "))
    h = float(input("ingrese valor para altura: "))
    triangulo(b, h)

else:
    print("opción invalida")
