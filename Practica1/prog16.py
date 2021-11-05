Boleta = 9+2+1
def inviertecad(cadena):
    if (len(cadena)%Boleta) == 0:
        cadena = cadena[::-1]
    return cadena

cadena = input("Escriba su numero de boleta: ")
print("\n Resultado: "+ inviertecad(cadena))