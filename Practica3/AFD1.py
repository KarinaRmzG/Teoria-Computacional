
Q=['q0','q1','q2']
Sigma=['a','b']
F=['q1']
s='q0'

delta= {('q0','a'):'q0',
	('q0','b'):'q1',
	('q1','a'):'q2',
	('q1','b'):'q2',
	('q2','a'):'q2',
	('q2','b'):'q2' }
print(Q,Sigma,F,s,delta)

w=['b','aaaab','ab','ba','aba','bb']

def transicion(estado,sigma):
	global Sigma,delta
	STATUS=True
	if sigma not in Sigma:
		STATUS=False
		return '',STATUS

	if(estado,sigma) not in delta.keys():
		STATUS=False
		return '',STATUS

	estado_siguiente = delta[(estado,sigma)]
	print("Transicion(",estado,",",sigma,")->",estado_siguiente)
	return estado_siguiente,STATUS
#modificable
transicion(s,'a')


for cadena in w:
	estado = s
	for c in cadena:
		estado,STATUS=transicion(estado,c)
		if not STATUS:
			break
	if STATUS and estado in F:
		print(cadena,"si esta en el lenguaje")
	else:
		print(cadena,"no esta en el lenguaje")
