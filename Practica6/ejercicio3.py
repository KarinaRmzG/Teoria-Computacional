tokens = ('a','b','c'); 
t_a = r'a'
t_b = r'b'
t_c = r'c'

def t_error(t):
	print("CARACTER ILEGAL ", t.value[0])
	t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
	''' S : A
		| empty '''
	pass

def p_A(p):
	''' A : a c A
		| c a A
		| a c A b B
		| c a A b B
		| C
		| empty '''

	pass

def p_B(p):
	''' B : b B
		| empty '''

	pass

def p_C(p):
	''' C : a c A b B a
		| c a A b B a
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
