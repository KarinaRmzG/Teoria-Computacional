numero=input("Escriba un numero: ")

# Jusitificación a la izquierda con diez caracteres, un decimal de precisión:

print(format(numero, '<10'))
# Jusitificación a la derecha con diez caracteres, un decimal de precisión:

print(format(numero, '>10'))

#centro
print (numero.center(10, " "))