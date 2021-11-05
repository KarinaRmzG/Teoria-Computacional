
import re
# Validando un RFC
cadena=input("Ingrese su RFC: ")
patron = ('^(([A-Z]|[a-z]|\s){4})(([0-9]){2})([0-1][0-9])([0-3][0-9])((([A-Z]|[a-z]|[0-9]){3}))$')

rfc = re.compile(patron)

rfc.search(cadena)

print(rfc.search(cadena))

