import ply.lex as lex

# Definimos los nombres de los tokens
tokens = (
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Definimos las expresiones regulares para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Una expresión regular para identificadores (que son una o más letras)
def t_ID(t):
    r'[a-zA-Z]+'
    return t

# Ignoramos los espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print("Error de lexer: Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Creamos el lexer
lexer = lex.lex()

# Ejemplo de uso
data = "x + y * (z - 2)"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
