from colorama import init, Fore, Style
from tokens import *
import re
#from tabulate import tabulate
# Para inicializar los colores de colorama y autoresetearlos
init(autoreset=True)

#Se crean las expresiones regulares
patron_identificador = r'[a-zA-Z]+'
patron_operador=r'[\+\-\*\/\=]'
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
        data.append([final,a,a,i])

    for b in identificador_numero:
        data.append(["NUMERO",b,b,i])

    for c in identificador_operador:
        data.append(["OPERADOR",c,c,i])    
        












    










print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))
archivo=open("codigo.txt","r")

col_width=12
data=[["IDENTIFICADOR","LEXEMA","LITERAL","LINEA"]]
print(Fore.BLUE + "{:{width}} {:{width}} {:{width}} {:{width}}".format(data[0][0], data[0][1],data[0][2],data[0][3], width=col_width) + Style.RESET_ALL)
print("-" * (col_width * 4))


i=0
for linea in archivo:
    i+=1
    analizador(i,linea.lower())

for row in data[1:]:
    print("{:{width}} {:{width}} {:{width}} {:{width}}".format(row[0], row[1],row[2], row[3], width=col_width-1))



