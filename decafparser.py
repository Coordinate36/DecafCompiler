from decaflexer import tokens
from decaflexer import precedence

def p_program(p):
    '''Program : ClassDef
               | Program ClassDef'''

def p_variable_def(p):
    '''VariableDef : Variable CommaID SEMICOLON
    '''

def p_variable(p):
    'Variable : Type ID'

def p_comma_id(p):
    '''CommaID : CommaID COMMA ID
               |
    '''

def p_type(p):
    '''Type : INT
            | FLOAT
            | BOOL
            | STRING
            | VOID
            | CLASS ID
            | Type LBRACKET RBRACKET
    '''

def p_variables(p):
    '''Variables : Variable
                 | Variables COMMA Variable
    '''

def p_formals(p):
    '''Formals : Variables
               |
    '''

def p_function_def(p):
    '''FunctionDef : Type ID LPAREN Formals RPAREN StmtBlock
                   | STATIC Type ID LPAREN Formals RPAREN StmtBlock
    '''

def p_class_def(p):
    '''ClassDef : CLASS ID LBRACE Fields RBRACE
                | CLASS ID EXTENDS ID LBRACE Fields RBRACE
    '''

def p_fields(p):
    '''Fields : Fields Field
              |
    '''

def p_field(p):
    '''Field : VariableDef
             | FunctionDef
    '''

def p_stmt_block(p):
    'StmtBlock : LBRACE Stmts RBRACE'

def p_stmts(p):
    '''Stmts : Stmts Stmt
             |
    '''

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

def p_simple_stmt(p):
    '''SimpleStmt : LValue ASSIGN Expr
                  | Call
                  |
    '''

def p_lvalue(p):
    '''LValue : ID
              | Expr DOT ID
              | Expr LBRACKET Expr RBRACKET
    '''

def p_call(p):
    '''Call : ID LPAREN Actuals RPAREN
            | Expr DOT ID LPAREN Actuals RPAREN
    '''

def p_actuals(p):
    '''Actuals : Exprs
               |
    '''

def p_for_stmt(p):
    'ForStmt : FOR LPAREN SimpleStmt SEMICOLON BoolExpr SEMICOLON SimpleStmt RPAREN Stmt'

def p_while_stmt(p):
    'WhileStmt : WHILE LPAREN BoolExpr RPAREN Stmt'

def p_if_stmt(p):
    '''IfStmt : IF LPAREN BoolExpr RPAREN Stmt %prec LOWER_THEN_ELSE
              | IF LPAREN BoolExpr RPAREN Stmt ELSE Stmt
    '''

def p_return_stmt(p):
    '''ReturnStmt : RETURN
                  | RETURN Expr
    '''

def p_break_stmt(p):
    'BreakStmt : BREAK'

def p_print_stmt(p):
    'PrintStmt : PRINT LPAREN Exprs RPAREN'

def p_exprs(p):
    '''Exprs : Expr
             | Exprs COMMA Expr
    '''

def p_bool_expr(p):
    'BoolExpr : Expr'

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

def p_expr_uminus(p):
    'Expr : MINUS Expr %prec UMINUS'

def p_constant(p):
    '''Constant : INT_CONST
                | FLOAT_CONST
                | BOOL_CONST
                | STR_CONST
                | NULL
    '''
    print(p[1])

def p_error(p):
    pass
