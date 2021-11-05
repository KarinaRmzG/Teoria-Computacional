cadena=input("Escriba una cadena: ")
car1=cadena[0:2]
car2=cadena[-2:]
nueva=car1+car2
longitud=len(cadena)
if longitud<2:
    print("Cadena vacia")
else:
    print(f"La cadena es {nueva}")