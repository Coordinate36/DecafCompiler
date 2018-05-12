from ply import lex

from GrammarTree import GrammarTree

reserved = {
    'bool': 'BOOL',
    'break': 'BREAK',
    'class': 'CLASS',
    'else': 'ELSE',
    'extends': 'EXTENDS',
    'float': 'FLOAT',
    'for': 'FOR',
    'if': 'IF',
    'int': 'INT',
    'new': 'NEW',
    'null': 'NULL',
    'return': 'RETURN',
    'string': 'STRING',
    'this': 'THIS',
    'void': 'VOID',
    'while': 'WHILE',
    'static': 'STATIC',
    'Print': 'PRINT',
    'ReadInteger': 'READINT',
    'ReadLine': 'READLINE',
    'instanceof': 'INSTANCEOF',
    'true': 'BOOL_CONST',
    'false': 'BOOL_CONST',
}

tokens = [
    'INT_CONST', 'STR_CONST', 'FLOAT_CONST', 'ID',
    'COMMENT',
    'ASSIGN',
    'PLUS', 'MINUS', 'MULTI', 'DIVIDE', 'MOD', 
    'AND', 'OR', 'EQUAL', 'NOTEQUAL', 'GREATER', 'GREATEREQUAL', 'LESS', 'LESSEQUAL', 'NOT',
    'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'LPAREN', 'RPAREN',
    'DOT', 'COMMA', 'SEMICOLON'
] + list(set(reserved.values()))

# precedence of the operators
precedence = (
    ('right', 'ASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'EQUAL', 'NOTEQUAL'),
    ('nonassoc', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTI', 'DIVIDE', 'MOD'),
    ('right', 'UMINUS', 'NOT'),
    ('left', 'DOT'),
    ('left', 'RBRACKET'),
    ('right', 'LBRACKET'),
    ('left', 'RPAREN'),
    ('right', 'LPAREN'),
    ('nonassoc', 'LOWER_THEN_ELSE'),
    ('nonassoc', 'ELSE'),
)

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    if t.type == 'BOOL_CONST':
        t.value = bool(t.value)
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_COMMENT(t):
    r'//.*|/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_PLUS(t):
    r'\+'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_MINUS(t):
    r'-'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_MULTI(t):
    r'\*'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_DIVIDE(t):
    r'/'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_MOD(t):
    r'%'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_AND(t):
    r'&&'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_OR(t):
    r'\|\|'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_EQUAL(t):
    r'=='
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_NOTEQUAL(t):
    r'!='
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_GREATER(t):
    r'>'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_GREATEREQUAL(t):
    r'>='
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_LESS(t):
    r'<'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_LESSEQUAL(t):
    r'<='
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_NOT(t):
    r'!'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_LBRACE(t):
    r'\{'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_RBRACE(t):
    r'\}'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_LBRACKET(t):
    r'\['
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t
    
def t_RBRACKET(t):
    r'\]'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_LPAREN(t):
    r'\('
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_RPAREN(t):
    r'\)'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_DOT(t):
    r'\.'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_COMMA(t):
    r','
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_SEMICOLON(t):
    r';'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_ASSIGN(t):
    r'='
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_STR_CONST(t):
    r'\".*?\"'
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_INT_CONST(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_FLOAT_CONST(t):
    r'[+-]?((\d+)(\.\d+)([eE](\+|-)?(\d+))? | (\d+)[eE](\+|-)?(\d+))'
    t.value = int(t.value)
    t.value = GrammarTree(t.type, t.lineno, (), t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print('Illegal character {0}'.format(t.value[0]))
    t.lexer.skip(1)
