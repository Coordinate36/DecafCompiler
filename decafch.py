from ply import lex
from ply import yacc

import decaflexer
import decafparser

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
logger = logging.getLogger()

filename = 'test1.decaf'

with open(filename) as f:
    code = f.read()

lexer = lex.lex(module=decaflexer)
lexer.input(code)
parser = yacc.yacc(module=decafparser, debug=True, debuglog=logger)
result = parser.parse(lexer=lexer, tracking=True, debug=logger)
