"""
author: john manyoma
@c0dejohn

fundamentos programación
Universidad Iberoamericana

2.Recibiendo diferentes tipos de datos y utilizando funciones
"""
#
print("""
        tipo de documento a elegir:
        
         1) C.C. (Cédula de Ciudadanía)
         2) T.I.(Tarjeta de Identidad)
         3) T.E. (Tarjeta Extranjeria)
          """)
tipo_documento = int(input("Elige un número de la lista:"))
print("\n completar los siguientes campos:")
numero_documento = int(input("\nnúmero del documento:"))
print("")
nombre = input("nombre: ")
print("")
edad = int(input("edad: "))
sexo = input("Sexo: (F)  ó (M)\n")
peso = float(input("\n peso en kg:"))
altura = float(input("alturan en cm:"))


def validar_edad(edad):
    if edad >= 18:
        return ("%s es mayor de edad" % nombre)
    else:
        return("%s es menor de edad" % nombre)


def peso_ideal(peso, sexo):
    if sexo == "f" or sexo == "F":
        ideal = 0.675 * altura - 52.0
        real = "Felicidades estás en el peso ideal" if ideal == peso else "No está en sú peso ideal"
        return real
    else:
        ideal = 0.75 * altura - 62.5
        real = "Felicidades estás en el peso ideal" if ideal == peso else "No estás en tú peso ideal"
        return real


validar_edad(edad)
peso_ideal(peso, sexo)
