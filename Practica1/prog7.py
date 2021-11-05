cadena=input("Escribe una cadena: ")

posicion=int(input("Ingrese la posicion del caracter que desea borrar: "))
o=cadena[posicion]
print(cadena.replace(o,""))