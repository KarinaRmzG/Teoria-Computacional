
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'a b c S : A\n\t\t| empty  A : a c A\n\t\t| c a A\n\t\t| a c A b B\n\t\t| c a A b B\n\t\t| C\n\t\t| empty  B : b B\n\t\t| empty  C : a c A b B a\n\t\t| c a A b B a\n\t\t| empty empty :'
    
_lr_action_items = {'a':([0,5,7,8,12,13,14,15,16,17,18,],[4,8,4,4,-14,-14,-14,19,-10,20,-9,]),'c':([0,4,7,8,],[5,7,5,5,]),'$end':([0,1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[-14,0,-1,-2,-7,-14,-14,-3,-8,-4,-14,-14,-14,-5,-10,-6,-9,-11,-12,]),'b':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[-7,-14,-14,12,-8,13,14,14,14,-5,-10,-6,-9,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'A':([0,7,8,],[2,9,11,]),'empty':([0,7,8,12,13,14,],[3,10,10,16,16,16,]),'C':([0,7,8,],[6,6,6,]),'B':([12,13,14,],[15,17,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> A','S',1,'p_S','ejercicio3.py',14),
  ('S -> empty','S',1,'p_S','ejercicio3.py',15),
  ('A -> a c A','A',3,'p_A','ejercicio3.py',19),
  ('A -> c a A','A',3,'p_A','ejercicio3.py',20),
  ('A -> a c A b B','A',5,'p_A','ejercicio3.py',21),
  ('A -> c a A b B','A',5,'p_A','ejercicio3.py',22),
  ('A -> C','A',1,'p_A','ejercicio3.py',23),
  ('A -> empty','A',1,'p_A','ejercicio3.py',24),
  ('B -> b B','B',2,'p_B','ejercicio3.py',29),
  ('B -> empty','B',1,'p_B','ejercicio3.py',30),
  ('C -> a c A b B a','C',6,'p_C','ejercicio3.py',35),
  ('C -> c a A b B a','C',6,'p_C','ejercicio3.py',36),
  ('C -> empty','C',1,'p_C','ejercicio3.py',37),
  ('empty -> <empty>','empty',0,'p_empty','ejercicio3.py',42),
]
