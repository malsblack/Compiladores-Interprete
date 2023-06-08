from colorama import init, Fore, Style
from AFD import *
import json
#from tabulate import tabulate
# Para inicializar los colores de colorama y autoresetearlos
init(autoreset=True)

tokens=json.load(open("tokens.json"))
palabras_reservadas=tokens["Palabas_reservadas"]
numeros=tokens["Numeros"]
operadores=tokens["Operadores"]


#se crean los arreglos en los cuales se van guardando los datos que alamcenamos para asi compararlos y posteriormente analizarlos
identificador=[]
operador=[]
numeros=[]
col_width=20
data=[]







def analizador(datos):
    for cadenas in datos:
        print(cadenas)

    for a in identificador_elemnto:
        final=tokens.get(a)
        
        if final==None:
            if a[0]=='"' or a[0]=="'":
                final="CADENA"
                data.append([final,a,a[1:-1],i])
            else:
                final="IDENTIFICADOR"
                data.append([final,a,a,i])

        else:
            data.append([final,a,"",i])
            
        

    for b in identificador_numero:
        data.append(["NUMERO",b,b,i])

    for c in identificador_operador:
        busqueda=tokens.get(c)
        data.append([str(busqueda),c,"",i])    
   


print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))

data=[["IDENTIFICADOR","LEXEMA","LITERAL","LINEA"]]
print(Fore.BLUE + "{:{width}} {:{width}} {:{width}} {:{width}}".format(data[0][0], data[0][1],data[0][2],data[0][3], width=col_width) + Style.RESET_ALL)
print("-" *  4)


analizador(lectura(open("codigo.txt")))

for row in data[1:]:
    print(Fore.GREEN+"{:{width}}".format(row[0],width=col_width),Fore.WHITE+ "{:{width}} {:{width}} {:{width}}".format(row[1],row[2], row[3], width=col_width-1))



