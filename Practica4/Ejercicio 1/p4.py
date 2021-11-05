from itertools import chain, combinations

def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

Q=['q0','q1']

Qprima=list(powerset(Q))

print("Qprima:",Qprima)

s='q0'

F=['q1']

Sigma=['a','b']

sprima=(s,)

print("sprima:",sprima)

Sigmaprima=Sigma

print("Sigmaprima:",Sigmaprima)

DELTA= { ('q0','a'): ['q0','q1'],
	 ('q0','b'): ['q1'],
	 ('q1','a'): [],
	 ('q1','b'): ['q0','q1']}

print("Construyendo Fprima:")
Fprima=[]
for x in Qprima:
	print(x)
	for q in x:
		print(q)
		if q in F:
			Fprima.append(x)
print("Fprima:")
print(Fprima)

print("Construyendo delta: ")
delta={}

for x in Qprima:
	for s in Sigmaprima:
		estados_siguientes=[]
		for q in x:
			estados_q_s=DELTA[(q,s)]
			for m in estados_q_s:
				if not (m in estados_siguientes):
					estados_siguientes.append(m)
		estados_siguientes.sort()
		delta[(x,s)]=tuple(estados_siguientes)

print("DELTA:")
print(delta)

#transiciones
def transicion(x,s):
	global delta,Sigmaprima
	if not (s in Sigmaprima):
		print(s,"NO ESTA EN EL ALFABETO")
		return False,''
	estado_siguiente=delta[(x,s)]
	return True,estado_siguiente
w=['aaab','','b','ba']

for c in w:
	estado=sprima
	for l in c:
		y,estado=transicion(estado,l)
	if y==True and (estado in Fprima):
		print(c,"SI ESTA EN EL LENGUAJE")
	else:
		print(c,"NO ESTA EN LE LENGUAJE")

