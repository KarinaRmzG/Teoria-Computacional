cadena1=input("Escriba una cadena: ")
l=len(cadena1)
if l<3:
    print(f"la cadena es: {cadena1}")
else:
    print("La cadena es:")
    print(cadena1[0:3])