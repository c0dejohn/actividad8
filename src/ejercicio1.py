"""
    autor: john manyoma

    Ejericicio 1: jugando con operadores

    """


def unitarios():
    suma = 5 + 5
    print("  resultado de la suma :%d " % suma)

    resta = 3-2
    print(" resultado de la resta:%d" % resta)


def asignacion():
    asignado = 1

    asignado += 2
    print(asignado)
    asignado -= 1
    print(asignado)
    asignado /= 2
    print(asignado)
    asignado *= 2
    print(asignado)
    asignado %= 2
    print(asignado)


def relacionales():
    a = 1
    b = 2
    c = int('1')

    print(a == c)
    print(a < b)
    print(a <= b)
    print(a > c)


def logicos():
    a = 'verde'
    b = 'amarillo'
    c = 'rojo'
    semaforo = a

    if semaforo == c or semaforo == b:
        print("no pasar")

    elif semaforo != ' amarillo' and semaforo == a:
        print('puede pasar')


def ternario():
    colombia = 5
    argentina = 0

    resultado = "gano colombia" if colombia > argentina else "perdió colombia"
    print(resultado)


print('operadores unitarios\n')
unitarios()

print('\n operadores asignación\n')
asignacion()

print('\n operadores relacionales\n')
relacionales()

print('\n operadores lógicos\n')
logicos()

print('\n operador ternario\n')
ternario()
