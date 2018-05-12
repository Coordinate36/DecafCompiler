from itertools import islice

from decaflexer import tokens
from decaflexer import precedence
from GrammarTree import GrammarTree

def p_program(p):
    '''Program : ClassDef
               | Program ClassDef'''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_variable_def(p):
    '''VariableDef : Variable CommaID SEMICOLON
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_variable(p):
    'Variable : Type ID'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_comma_id(p):
    '''CommaID : CommaID COMMA ID
               |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_type(p):
    '''Type : INT
            | FLOAT
            | BOOL
            | STRING
            | VOID
            | CLASS ID
            | Type LBRACKET RBRACKET
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_variables(p):
    '''Variables : Variable
                 | Variables COMMA Variable
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_formals(p):
    '''Formals : Variables
               |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_function_def(p):
    '''FunctionDef : Type ID LPAREN Formals RPAREN StmtBlock
                   | STATIC Type ID LPAREN Formals RPAREN StmtBlock
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_class_def(p):
    '''ClassDef : CLASS ID LBRACE Fields RBRACE
                | CLASS ID EXTENDS ID LBRACE Fields RBRACE
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_fields(p):
    '''Fields : Fields Field
              |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_field(p):
    '''Field : VariableDef
             | FunctionDef
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_stmt_block(p):
    'StmtBlock : LBRACE Stmts RBRACE'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_stmts(p):
    '''Stmts : Stmts Stmt
             |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_stmt(p):
    '''Stmt : VariableDef
            | SimpleStmt SEMICOLON
            | IfStmt
            | WhileStmt
            | ForStmt
            | BreakStmt SEMICOLON
            | ReturnStmt SEMICOLON
            | PrintStmt SEMICOLON
            | StmtBlock
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_simple_stmt(p):
    '''SimpleStmt : LValue ASSIGN Expr
                  | Call
                  |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_lvalue(p):
    '''LValue : ID
              | Expr DOT ID
              | Expr LBRACKET Expr RBRACKET
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_call(p):
    '''Call : ID LPAREN Actuals RPAREN
            | Expr DOT ID LPAREN Actuals RPAREN
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_actuals(p):
    '''Actuals : Exprs
               |
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_for_stmt(p):
    'ForStmt : FOR LPAREN SimpleStmt SEMICOLON BoolExpr SEMICOLON SimpleStmt RPAREN Stmt'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_while_stmt(p):
    'WhileStmt : WHILE LPAREN BoolExpr RPAREN Stmt'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_if_stmt(p):
    '''IfStmt : IF LPAREN BoolExpr RPAREN Stmt %prec LOWER_THEN_ELSE
              | IF LPAREN BoolExpr RPAREN Stmt ELSE Stmt
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_return_stmt(p):
    '''ReturnStmt : RETURN
                  | RETURN Expr
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_break_stmt(p):
    'BreakStmt : BREAK'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_print_stmt(p):
    'PrintStmt : PRINT LPAREN Exprs RPAREN'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_exprs(p):
    '''Exprs : Expr
             | Exprs COMMA Expr
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_bool_expr(p):
    'BoolExpr : Expr'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_expr(p):
    '''Expr : Constant
            | LValue
            | THIS
            | Call
            | LPAREN Expr RPAREN
            | Expr PLUS Expr
            | Expr MINUS Expr
            | Expr MULTI Expr
            | Expr DIVIDE Expr
            | Expr MOD Expr
            | Expr LESS Expr
            | Expr LESSEQUAL Expr
            | Expr GREATER Expr
            | Expr GREATEREQUAL Expr
            | Expr EQUAL Expr
            | Expr NOTEQUAL Expr
            | Expr AND Expr
            | Expr OR Expr
            | NOT Expr
            | READINT LPAREN RPAREN
            | READLINE LPAREN RPAREN
            | NEW ID LPAREN RPAREN
            | NEW Type LBRACKET Expr RBRACKET
            | INSTANCEOF LPAREN Expr COMMA ID RPAREN
            | LPAREN CLASS ID RPAREN Expr
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_expr_uminus(p):
    'Expr : MINUS Expr %prec UMINUS'
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_constant(p):
    '''Constant : INT_CONST
                | FLOAT_CONST
                | BOOL_CONST
                | STR_CONST
                | NULL
    '''
    p[0] = GrammarTree(p.slice[0], p.lineno(0), p[1:])

def p_error(p):
    pass
