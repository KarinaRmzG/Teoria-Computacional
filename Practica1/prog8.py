cadena1=input("Escribe una cadena: ")
p= cadena1[:1]
r = cadena1[-1:]
cadena1=r+cadena1[1:(len(cadena1)-1)]+p
print("La nueva cadena es: "+cadena1)
