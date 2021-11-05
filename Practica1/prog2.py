cadena=input("Escribe una cadena: ")

def frecuencia(cadena):
    cad = dict()
    for caracter in cadena:
        if caracter in cad.keys():
            cad[caracter] = cad[caracter] + 1
        else:
            cad[caracter] = 1
    return cad

print(frecuencia(cadena))