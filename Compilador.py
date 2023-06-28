from AnalizadorLexico import analizador_lexico
from AnalizadorSintantico import *
import sys

resultado_lexico=analizador_lexico(sys.argv[1])
analizador_sintactico(resultado_lexico)