from colorama import init, Fore, Style
from tokens import *
import re
# Para inicializar los colores de colorama y autoresetearlos
init(autoreset=True)

#Se crean las expresiones regulares

patron_identificador = r'[a-zA-Z]+'
patron_numero = r'\d+'
patron_y=r'\by\b'
patron_clase=r'\bclase\b'
patron_ademas=r'\bademas\b'
patron_falso=r'\bfalso\b'
patron_para=r'\bpara\b'
patron_fun=r'\bfun\b'
patron_si=r'\bsi\b'
patron_nulo=r'\bnulo\b'
patron_o=r'\bo\b'
patron_imprimir=r'\bimprimir\b'
patron_retornar=r'\bretornar\b'
patron_super=r'\bsuper\b'
patron_este=r'\beste\b'
patron_verdadero=r'\bverdadero\b'
patron_var=r'\bvar\b'
patron_mientras=r'\bmientras\b'
patron_identificador=r'\bidentificador\b'
patron_cadena=r'\bcadena\b'
patron_numero=r'\bnumero\b'






def analizador(i,linea):
    coincidencia=re.findall(patron_identificador,linea)
    print(coincidencia)






print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))
archivo=open("codigo.txt","r")

i=0
for linea in archivo:
    i+=1
    analizador(i,linea)




