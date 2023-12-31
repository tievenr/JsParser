
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA DIVIDE DQUOTE FUNCTION IDENTIFIER LBRACE LPAREN MINUS NUMBER PLUS PRINT RBRACE RETURN RPAREN SEMICOLON TIMES\n    function : FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE\n            | FUNCTION IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE\n    parameters : parameter\n                  | parameter COMMA parametersparameter : IDENTIFIERstatements : statement\n                  | statement statementsstatement : assignment_statement\n                 | print_statement\n                 | returnreturn : RETURN expression SEMICOLON\n    assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON\n                         | IDENTIFIER SEMICOLON\n    print_statement : PRINT LPAREN expression RPAREN SEMICOLONexpression : IDENTIFIER\n                  | NUMBER\n                  | expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | DQUOTE sentences DQUOTEsentences : sentence\n                 | sentence sentencessentence :  IDENTIFIER\n                  | NUMBER\n                  | sentence PLUS\n                  | sentence MINUS\n                  | sentence PLUS sentence\n                  | sentence MINUS sentence\n                  | sentence TIMES sentence\n                  | sentence DIVIDE sentence'
    
_lr_action_items = {'FUNCTION':([0,],[2,]),'$end':([1,25,32,],[0,-2,-1,]),'IDENTIFIER':([2,4,10,11,12,15,16,17,18,20,23,24,27,31,35,36,37,38,39,41,42,43,44,52,53,54,55,56,57,58,59,60,],[3,5,13,5,13,13,-8,-9,-10,29,29,-13,29,42,-11,29,29,29,29,42,-24,-25,-12,42,42,42,42,-14,-28,-29,-30,-31,]),'LPAREN':([3,19,],[4,27,]),'RPAREN':([4,5,6,8,21,29,30,34,46,47,48,49,50,],[7,-5,9,-3,-4,-15,-16,45,-17,-18,-19,-20,-21,]),'COMMA':([5,8,],[-5,11,]),'LBRACE':([7,9,],[10,12,]),'PRINT':([10,12,15,16,17,18,24,35,44,56,],[19,19,19,-8,-9,-10,-13,-11,-12,-14,]),'RETURN':([10,12,15,16,17,18,24,35,44,56,],[20,20,20,-8,-9,-10,-13,-11,-12,-14,]),'ASSIGN':([13,],[23,]),'SEMICOLON':([13,28,29,30,33,45,46,47,48,49,50,],[24,35,-15,-16,44,56,-17,-18,-19,-20,-21,]),'RBRACE':([14,15,16,17,18,22,24,26,35,44,56,],[25,-6,-8,-9,-10,32,-13,-7,-11,-12,-14,]),'NUMBER':([20,23,27,31,36,37,38,39,41,42,43,52,53,54,55,57,58,59,60,],[30,30,30,43,30,30,30,30,43,-24,-25,43,43,43,43,-28,-29,-30,-31,]),'DQUOTE':([20,23,27,36,37,38,39,40,41,42,43,51,52,53,57,58,59,60,],[31,31,31,31,31,31,31,50,-22,-24,-25,-23,-26,-27,-28,-29,-30,-31,]),'PLUS':([28,29,30,33,34,41,42,43,46,47,48,49,50,52,53,57,58,59,60,],[36,-15,-16,36,36,52,-24,-25,36,36,36,36,-21,-26,-27,52,52,52,52,]),'MINUS':([28,29,30,33,34,41,42,43,46,47,48,49,50,52,53,57,58,59,60,],[37,-15,-16,37,37,53,-24,-25,37,37,37,37,-21,-26,-27,53,53,53,53,]),'TIMES':([28,29,30,33,34,41,42,43,46,47,48,49,50,52,53,57,58,59,60,],[38,-15,-16,38,38,54,-24,-25,38,38,38,38,-21,-26,-27,54,54,54,54,]),'DIVIDE':([28,29,30,33,34,41,42,43,46,47,48,49,50,52,53,57,58,59,60,],[39,-15,-16,39,39,55,-24,-25,39,39,39,39,-21,-26,-27,55,55,55,55,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'function':([0,],[1,]),'parameters':([4,11,],[6,21,]),'parameter':([4,11,],[8,8,]),'statements':([10,12,15,],[14,22,26,]),'statement':([10,12,15,],[15,15,15,]),'assignment_statement':([10,12,15,],[16,16,16,]),'print_statement':([10,12,15,],[17,17,17,]),'return':([10,12,15,],[18,18,18,]),'expression':([20,23,27,36,37,38,39,],[28,33,34,46,47,48,49,]),'sentences':([31,41,],[40,51,]),'sentence':([31,41,52,53,54,55,],[41,41,57,58,59,60,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> function","S'",1,None,None,None),
  ('function -> FUNCTION IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE','function',8,'p_function','yacc_func.py',6),
  ('function -> FUNCTION IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE','function',7,'p_function','yacc_func.py',7),
  ('parameters -> parameter','parameters',1,'p_parameters','yacc_func.py',15),
  ('parameters -> parameter COMMA parameters','parameters',3,'p_parameters','yacc_func.py',16),
  ('parameter -> IDENTIFIER','parameter',1,'p_parameter','yacc_func.py',23),
  ('statements -> statement','statements',1,'p_statements','yacc_func.py',27),
  ('statements -> statement statements','statements',2,'p_statements','yacc_func.py',28),
  ('statement -> assignment_statement','statement',1,'p_statement','yacc_func.py',35),
  ('statement -> print_statement','statement',1,'p_statement','yacc_func.py',36),
  ('statement -> return','statement',1,'p_statement','yacc_func.py',37),
  ('return -> RETURN expression SEMICOLON','return',3,'p_return','yacc_func.py',41),
  ('assignment_statement -> IDENTIFIER ASSIGN expression SEMICOLON','assignment_statement',4,'p_assignment_statement','yacc_func.py',46),
  ('assignment_statement -> IDENTIFIER SEMICOLON','assignment_statement',2,'p_assignment_statement','yacc_func.py',47),
  ('print_statement -> PRINT LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','yacc_func.py',55),
  ('expression -> IDENTIFIER','expression',1,'p_expression','yacc_func.py',59),
  ('expression -> NUMBER','expression',1,'p_expression','yacc_func.py',60),
  ('expression -> expression PLUS expression','expression',3,'p_expression','yacc_func.py',61),
  ('expression -> expression MINUS expression','expression',3,'p_expression','yacc_func.py',62),
  ('expression -> expression TIMES expression','expression',3,'p_expression','yacc_func.py',63),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','yacc_func.py',64),
  ('expression -> DQUOTE sentences DQUOTE','expression',3,'p_expression','yacc_func.py',65),
  ('sentences -> sentence','sentences',1,'p_sentences','yacc_func.py',75),
  ('sentences -> sentence sentences','sentences',2,'p_sentences','yacc_func.py',76),
  ('sentence -> IDENTIFIER','sentence',1,'p_sentence','yacc_func.py',83),
  ('sentence -> NUMBER','sentence',1,'p_sentence','yacc_func.py',84),
  ('sentence -> sentence PLUS','sentence',2,'p_sentence','yacc_func.py',85),
  ('sentence -> sentence MINUS','sentence',2,'p_sentence','yacc_func.py',86),
  ('sentence -> sentence PLUS sentence','sentence',3,'p_sentence','yacc_func.py',87),
  ('sentence -> sentence MINUS sentence','sentence',3,'p_sentence','yacc_func.py',88),
  ('sentence -> sentence TIMES sentence','sentence',3,'p_sentence','yacc_func.py',89),
  ('sentence -> sentence DIVIDE sentence','sentence',3,'p_sentence','yacc_func.py',90),
]
