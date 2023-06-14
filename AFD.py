from colorama import init, Fore, Style
import json
from AnalizadorSintantico import analizador_sintantico

tokens=json.load(open("tokens.json"))
palabras_reservadas=tokens["Palabas_reservadas"]
numeros=tokens["Numeros"]
operadores=tokens["Operadores"]
operadores_especiales=tokens["Operadores_especiales"]
novalidos=[]
col_width=20
data=[]
data2=[]


def seperacion(lista):
    nueva_lista=[]
    for elemento in lista:
        if elemento[0][0] not in operadores:
            pass
        else:
            if elemento[0][0:2] in operadores:
                pass
            else:
                if elemento[0][0:2] not in operadores_especiales:
                    for i in elemento[0][0:2]:
                        lista.insert(lista.index(elemento),[i,elemento[1]])
                    lista.pop(lista.index(elemento))
                else:
                    pass
def escritura(lista):
    for elemento in lista:
        if elemento[0] in palabras_reservadas:
            data2.append([palabras_reservadas.get(elemento[0]),elemento[0],elemento[0],elemento[1]])
        elif elemento[0][0]=='"':
            data2.append(["CADENA",elemento[0],elemento[0][1:-1],elemento[1]])
        elif elemento[0] in operadores:
            data2.append([operadores.get(elemento[0]),elemento[0],"",elemento[1]])
        elif elemento[0] in operadores_especiales:
            data2.append([operadores_especiales.get(elemento[0]),elemento[0],"",elemento[1]])
        elif elemento[0]=="NUMERO":
            data2.append([elemento[0],elemento[1],elemento[2],elemento[3]])
        else:
            data2.append(["IDENTIFICADOR",elemento[0],elemento[0],elemento[1]])
def lectura(archivo):
    aux=False
    for reglon,linea in enumerate(archivo):

        palabra="" 
        constructor_numero=""  
        constructor_operador=""
        cadena=""
        comentario=""
        
        for indice,caracter in enumerate(linea):
            if caracter.isalpha(): #Validacion letras
                if comentario!="":
                    comentario+=caracter
                else:
                    if cadena!="":
                        cadena+=caracter
                    else:
                        palabra+=caracter
                        if constructor_operador!="":
                            data.append([constructor_operador,reglon+1])
                            constructor_operador=""

                    

            elif caracter in numeros: #Validacion numeros
                if comentario!="":
                    comentario+=caracter
                else:
                    if cadena!="":
                        cadena+=caracter
                    else:
                        if palabra !="":
                            palabra+=caracter
                        else:
                            constructor_numero+=caracter
                            
                        if constructor_operador!="":
                            data.append([constructor_operador,reglon+1])
                            constructor_operador=""

            elif caracter in operadores: #validacion operadores
                    
                if cadena!="":
                    cadena+=caracter
                else:
                    if palabra!="":
                        data.append([palabra,reglon+1])
                        palabra=""
                    if constructor_numero!="":
                        data.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                        constructor_numero=""
                    if constructor_operador!="":
                        constructor_operador+=caracter
                    else:
                        constructor_operador+=caracter
                    if constructor_operador=="/*":
                        comentario+=constructor_operador
                        constructor_operador=""
                    elif constructor_operador=="*/":
                        comentario+=constructor_operador
                        data.append(["COMENTARIO",comentario,comentario[2:-2],reglon+1])
                        constructor_operador=""
                    
                    
                    
            elif caracter=='"':
                if comentario!="":
                    comentario+=caracter
                else:
                    if palabra!="":
                        palabras.append([palabra,reglon+1])
                        palabra=""
                    if constructor_numero!="":
                        data.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                        constructor_numero=""
                    if constructor_operador!="":
                        data.append([constructor_operador,reglon+1])
                        constructor_operador=""
                    if cadena=="":
                        cadena+=caracter
                    else:
                        if cadena.count('"')==1:
                            cadena+=caracter
                            data.append([cadena,reglon+1])
                            cadena=""
                        else:
                            pass
                    
                    
            elif caracter ==" ":
                if palabra!="":
                    data.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    data.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                    constructor_numero=""
                if cadena!="":
                    cadena+=caracter
                if comentario!="":
                    comentario+=caracter                
            else:
                novalidos.append([caracter,reglon])
            if indice==len(linea)-1:
                if comentario!="":
                    pass
                else:
                    if palabra!="":
                        data.append([palabra,reglon+1])
                    elif constructor_numero!="":
                        data.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                    elif constructor_operador!="":
                        data.append([constructor_operador,reglon+1])
                    else:
                        pass


  

                
print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))

data2=[["IDENTIFICADOR","LEXEMA","LITERAL","LINEA"]]
print(Fore.BLUE + "{:{width}} {:{width}} {:{width}} {:{width}}".format(data2[0][0], data2[0][1],data2[0][2],data2[0][3], width=col_width) + Style.RESET_ALL)
print("-" *  4)

lectura(open("codigo.txt"))
seperacion(data)
escritura(data)
analizador_sintantico(data2)
    
#for row in data2[1:]:
    #print(row)
    #print(Fore.GREEN+"{:{width}}".format(row[0],width=col_width),Fore.WHITE+ "{:{width}} {:{width}} {:{width}}".format(row[1],row[2], row[3], width=col_width-1))