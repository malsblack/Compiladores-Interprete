import re

# Definimos los patrones de las expresiones regulares
patron_id = r'[a-zA-Z]+'
patron_num = r'\d+'
patron_op = r'[+\-*/]'

# Definimos la función que analiza la cadena de entrada y devuelve los tokens
def analizador_lexico(cadena):
    tokens = []
    while cadena:
        # Ignoramos los espacios en blanco y saltos de línea
        if cadena[0] in [' ', '\n']:
            cadena = cadena[1:]
            continue
        # Buscamos un identificador
        m = re.match(patron_id, cadena)
        if m:
            tokens.append(('ID', m.group()))
            cadena = cadena[m.end():]
            continue
        # Buscamos un número entero
        m = re.match(patron_num, cadena)
        if m:
            tokens.append(('NUM', int(m.group())))
            cadena = cadena[m.end():]
            continue
        # Buscamos un operador matemático
        m = re.match(patron_op, cadena)
        if m:
            tokens.append(('OP', m.group()))
            cadena = cadena[m.end():]
            continue
        # Si no se encuentra ningún patrón, se ha encontrado un caracter inválido
        raise ValueError("Caracter inválido en la cadena de entrada")
    return tokens

# Ejemplo de uso
cadena = "gola + ll"
tokens = analizador_lexico(cadena)
print(tokens)
