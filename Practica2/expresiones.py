import re
# Validando una dirección IP
cadena=input("Ingrese una direccion IP: ")
patron = ('^(?:(?:25[0-5]|2[0-4][0-9]|'
          '[01]?[0-9][0-9]?)\.){3}'
          '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

ip = re.compile(patron)


ip.search(cadena)



print(ip.search(cadena))


