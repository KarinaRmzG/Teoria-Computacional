LONG_LLAVE = 26


def getOpc():
    print('Escribir "encriptar", "e" o "desencriptar", "d".')
    while True:

        print('¿Desea encriptar o desencriptar el mensaje?')

        option = input().lower()
        if option in ('encriptar y desencriptar d').split():
            return option
    else:
        print('adios')



def getMsj():
    print('Escribe el mensaje:')
    return input()


def getLlave():
    llave = 0
    while True:
        print('Ingresar la llave (1-%s)' % (LONG_LLAVE))
        llave = int(input())
        if (llave >= 1 and llave <= LONG_LLAVE):
            return llave


def getTraducirMsj(option, mensaje, llave):
    if option[0] == 'd':
        llave = -llave
    traducir = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += llave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traducir += chr(num)
        else:
            traducir += simbolo
    return traducir


option = getOpc()
mensaje = getMsj()
llave = getLlave()

print('El texto traducido es:')
print(getTraducirMsj(option, mensaje, llave))