Sigma=['a','b']
#Q=['q0',q1']
F=['q4']
s='q1'
z='Z'

delta={ ('q1','a','Z') : ('q2','BZ'),
	('q2','a','B') : ('q2','BB'),
	('q2','b','B') : ('q3',''),
	('q3','b','B') : ('q3',''),
	('q3','','Z') : ('q4','Z')
	}

pila=[z]

def transicion(estado,sigma,gamma):
	global delta,pila

	if (estado,sigma,gamma) not in delta.keys():
		print("Error")
		exit(0)
	t=delta[(estado,sigma,gamma)]
	print( (estado,sigma,gamma), "->", t)
	for g in t[1][::-1]:
		pila.append(g)
	print("pila:",pila[::-1])
	return t[0]

def procesa_cadena(w):
	global s,pila
	estado=s
	pila=[z]
	for sigma in w:
	#	print("1",pila)
		gamma=pila.pop()
	#	print("2",pila)
		estado= transicion(estado,sigma,gamma)
	gamma=pila.pop()
	if (estado,'',gamma) in delta.keys():
		t=delta[(estado,'',gamma)]
		print( (estado,'',gamma), "->", t)
		estado=t[0]

		for g in t[1][::-1]:
			pila.append(g)
		print("pila",pila[::-1])

	if estado in F:
		print("\t",w,"PERTENECE AL LENGUAJE")
	else:
		print("\t",w,"NO PERTENECE AL LENGUAJE")

cadenas=['a','ab','aaabbb','aabb','ba']

for w in cadenas:
	procesa_cadena(w)
