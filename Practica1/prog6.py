cadena=input("Escribe palabras separadas por espacios: ")
def maxpal(listaP):
    tam=0
    tamMax=0
    for elemeto in listaP:
        tam=len(elemeto)
        if tam>tamMax:
            tamMax=tam
    return tamMax
listaP=cadena.split()
print("El tamaño de la cadena mas larga es: " +str(maxpal(listaP)))