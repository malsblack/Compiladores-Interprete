from colorama import init, Fore, Style
from tokens import *
import re
# Para inicializar los colores de colorama y autoresetearlos
init(autoreset=True)

#Se crean las expresiones regulares
patron_identificador = r'[a-zA-Z]+'
patron_operador=r'[({+\-*/})]'
patron_num = r'\d+'

identificador=[]
operador=[]
numeros=[]







def analizador(i,linea):
    identificador_elemnto=(re.findall(patron_identificador,linea))
    identificador_numero=(re.findall(patron_num,linea))
    identificador_operador=(re.findall(patron_operador,linea))

    for a in identificador_elemnto:
        final=tokens.get(a)
        if final==None:
            final="CADENA"
        print(f"Identificador: {final}, Lexema: {a}, Literal: {a}, Linea: {i}")
    
    for b in identificador_numero:
        print(f"Identificador: NUMERO , Lexema: {b}, Literal: {b}, Linea: {i}")
        












    










print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))
archivo=open("codigo.txt","r")

i=0
for linea in archivo:
    i+=1
    analizador(i,linea.lower())




