cadena=input("Escribe una cadena: ")

car = cadena[:1]
aux = 'a'
aux1 = 'e'
aux2 = 'i'
aux3 = 'o'
aux4 = 'u'


if car == aux or car == aux1 or car == aux2 or car == aux3 or car==aux4:
    print(f"La palabra {cadena} SI empieza con los caracteres especificados")
else:
    print(f"La palabra {cadena} NO empieza con los caracteres especificados")
