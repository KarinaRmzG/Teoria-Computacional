cadena1=input("Escriba una cadena: ")
l=len(cadena1)
if l%2==0:
    a=int(len(cadena1)/2)
    print(cadena1[:a])
else:
    print("La cadena es de longitud impar")