from ply import lex

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

t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_GREATEREQUAL = r'>='
t_LESS = r'<'
t_LESSEQUAL = r'<='
t_NOT = r'!'

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'

t_STR_CONST = r'\".*?\"'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    if t.type == 'BOOL_CONST':
        t.value = bool(t.value)
    return t

def t_INT_CONST(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_FLOAT_CONST(t):
    r'[+-]?((\d+)(\.\d+)([eE](\+|-)?(\d+))? | (\d+)[eE](\+|-)?(\d+))'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENT(t):
    r'//.*|/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print('Illegal character {0}'.format(t.value[0]))
    t.lexer.skip(1)
