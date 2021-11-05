abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def cadM(cadena,cad1):
    contM=0
    for cont in cad1:
        if cont in abecedario:
            contM+=1
        if contM== 2:
            return cadena.upper()
    return cadena

cadena = input("Escribe una cadena: ")
print("\n Resultado: "+cadM(cadena,cadena[0:4]))