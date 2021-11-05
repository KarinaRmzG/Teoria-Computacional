
cad1= 'Hola mundo'
print(cad1)
pref = input("Ingrese el prefijo que desee agregar: ")
lista=[]
for i in cad1:
    lista= cad1.split()
indice= 0
for i in lista:
    lista[indice]= pref+ lista[indice]
    indice+=1
cad2= " ".join(lista)
print(cad2)