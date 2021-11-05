cadena= []
aux = []
cadena=input("Escribe una cadena: ")
i = 0
for j in cadena:
    if i % 2 == 0:
        aux.append(j)
    i = i + 1
print("".join(aux))