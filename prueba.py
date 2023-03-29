import re

pattern = r'^([\'"]\w+[\'"]|\w+)$'

value = "hola"
if re.match(pattern, value):
    print('La cadena de texto es válida')
else:
    print('La cadena de texto es inválida')
