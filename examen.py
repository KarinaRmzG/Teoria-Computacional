from itertools import chain, combinations

def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

Q=['q0','q1','q2','q3','q4','q5']

Qprima=list(powerset(Q))

print("\tQprima:")
print("===================================")
print(Qprima)
print("\n")

s='q0'

F=['q2','q4','q5']

Sigma=['a','b','c']

sprima=(s,)

print("\tsprima:")
print("===================================")
print(sprima)
print("\n")

Sigmaprima=Sigma

print("\tSigmaprima:")
print("===================================")
print(Sigmaprima)
print("\n")

DELTA = { ('q0','a'): ['q0','q3'],
	  ('q0','b'): ['q0','q1'],
	  ('q0','c'): [],
	  ('q1','a'): [],
          ('q1','b'): ['q2'],
	  ('q1','c'): [],
	  ('q2','a'): ['q2'],
          ('q2','b'): ['q2'],
	  ('q2','c'): [],
	  ('q3','a'): ['q4'],
	  ('q3','b'): [],
	  ('q3','c'): ['q5'],
     	  ('q4','a'): ['q4'],
     	  ('q4','b'): ['q4'],
	  ('q4','c'): [],
	  ('q5','a'): [],
	  ('q5','b'): [],
	  ('q5','c'): []}

print("\tConstruyendo Fprima:")
print("====================================")
Fprima=[]
for x in Qprima:
	print(x)
	for q in x:
		print(q)
		if q in F:
			Fprima.append(x)
print("\n")
print("\tFprima:")
print("===================================")
print(Fprima)
print("\n")
#print("\tConstruyendo delta: ")
#print("===================================")
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
print("\n")
print("\tDELTA:")
print("===================================")
print(delta)
print("\n")
#transiciones

print("\tTRANSICIONES")
print("===================================")
print("\n")

def transicion(x,s):
	global delta,Sigmaprima
	if not (s in Sigmaprima):
		print(s,"NO ESTA EN EL ALFABETO")
		return False,''
	estado_siguiente=delta[(x,s)]
	print("Transición: \t(", estado,",",Sigmaprima,") --->",estado_siguiente)
	return True,estado_siguiente
w =['bb','aa','abbaba','ac','bac','bc','','a','b','c']

for c in w:
	estado=sprima
	for l in c:
		y,estado=transicion(estado,l)
	if y==True and (estado in Fprima):
		print("\tLa cadena:",c,"SI ESTA EN EL LENGUAJE\n")
	else:
		print("\tLa cadena:",c,"NO ESTA EN EL LENGUAJE\n")

