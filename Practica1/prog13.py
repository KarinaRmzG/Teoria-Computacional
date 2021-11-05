cadena1=input("Escriba una cadena: ")
l=len(cadena1)
if l<2:
    print("Fin del programa")
else:
    print("La cadena es:")
    print(cadena1[-2:]*4)