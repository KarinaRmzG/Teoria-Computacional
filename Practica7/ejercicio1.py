tokens = ('a','b'); 
t_a = r'a'
t_b = r'b'

def t_error(t):
	print("CARACTER ILEGAL ", t.value[0])
	t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
	''' S : a S b
		| empty '''
	pass


def p_empty(p):
	'empty :'
	pass

s=' '

def p_error(p):
	global s
	if p: 
		print("ERROR DE SINTAXIS EN", p.value)
		print(s,"NO ESTA EN EL LENGUAJE")
	else:
		print("ERROR DE SINTAXIS EN EOF")
		print(s,"NO ESTA EN EL LENGUAJE")


import ply.yacc as yacc
yacc.yacc()

while 1:
	try:
		s = input('>')
	except EOFERROR:
		break
	if not s:
		continue
	t = yacc.parse(s) 



