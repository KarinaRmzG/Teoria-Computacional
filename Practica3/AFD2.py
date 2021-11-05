Q=['q0','q1','q2']
Sigma=['a','b']
F=['q0','q1']
s='q0'

delta={ ('q0','a'):'q1',
	('q0','b'):'q0',
	('q1','a'):'q2',
	('q1','b'):'q0',
	('q2','a'):'q2',
	('q2','b'):'q2' }
print(Q,Sigma,F,s,delta)

w=['a','b','ab','abababa','aab','abaab','abaaaab'] 

def transicion(estado,sigma):
	global Sigma,delta
	STATUS=True
	if sigma not in Sigma:
		STATUS=False
		return '',STATUS

	if(estado,sigma) not in delta.keys():
		STATUS=False
		return '',STATUS

	estado_siguiente=delta[(estado,sigma)]
	print("TRANSICION(",estado,",",sigma,")--->",estado_siguiente)
	return estado_siguiente,STATUS

transicion(s,'b')


for cadena in w:
	estado = s
	for c in cadena:
		estado,STATUS=transicion(estado,c)
		if not STATUS:
			break
	if STATUS and estado in F:
		print(cadena,"SI ESTA EN EL LENGUAJE")
	else:
		print(cadena,"NO ESTA EN EL LENGUAJE")
