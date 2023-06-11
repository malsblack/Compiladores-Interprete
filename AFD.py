from colorama import init, Fore, Style
import json
tokens=json.load(open("tokens.json"))
palabras_reservadas=tokens["Palabas_reservadas"]
numeros=tokens["Numeros"]
operadores=tokens["Operadores"]
operadores_especiales=tokens["Operadores_especiales"]
palabras=[]
numeros_lista=[]  
operadores_lista=[]
novalidos=[]
col_width=20
data=[]
def seperacion(lista):
    nueva_lista=[]
    for elemento in lista:
        if elemento[0] in operadores_especiales:
            nueva_lista.append(elemento)
        else:
            for i in elemento[0]:
                nueva_lista.append([i,elemento[1]])

    return(nueva_lista)
    
def escritura(lista):
    for elemento in lista:
        
        if elemento[0] in palabras_reservadas:
            data.append([palabras_reservadas.get(elemento[0]),elemento[0],elemento[0],elemento[1]])
        elif elemento[0][0]=='"':
            data.append(["CADENA",elemento[0],elemento[0][1:-1],elemento[1]])
        elif elemento[0] in operadores:
            data.append([operadores.get(elemento[0]),elemento[0],"",elemento[1]])
        elif elemento[0] in operadores_especiales:
            data.append([operadores_especiales.get(elemento[0]),elemento[0],"",elemento[1]])
        elif elemento[0]=="NUMERO":
            data.append([elemento[0],elemento[1],elemento[2],elemento[3]])
        else:
            data.append(["IDENTIFICADOR",elemento[0],elemento[0],elemento[1]])
            
def lectura(archivo):
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
                            operadores_lista.append([constructor_operador,reglon+1])
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
                            operadores_lista.append([constructor_operador,reglon+1])
                            constructor_operador=""

            elif caracter in operadores: #validacion operadores
                if cadena!="":
                    cadena+=caracter
                else:
                    if palabra!="":
                        palabras.append([palabra,reglon+1])
                        palabra=""
                    if constructor_numero!="":
                        numeros_lista.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                        constructor_numero=""
                    if constructor_operador!="":
                        constructor_operador+=caracter
                    else:
                        constructor_operador+=caracter
                if constructor_operador=="*/":
                    comentario+=constructor_operador
                    constructor_operador=""
                elif constructor_operador=="/*":
                    comentario+=constructor_operador
                    data.append(["COMENTARIO",comentario,comentario,reglon+1])
                    
                    
                    
            elif caracter=='"':
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    numeros_lista.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                    constructor_numero=""
                if constructor_operador!="":
                    operadores_lista.append([constructor_operador,reglon+1])
                    constructor_operador=""
                if cadena=="":
                    cadena+=caracter
                else:
                    if cadena.count('"')==1:
                        cadena+=caracter
                        palabras.append([cadena,reglon+1])
                        cadena=""
                    else:
                        pass
                
                    
            elif caracter ==" ":
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    numeros_lista.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                    constructor_numero=""
                if cadena!="":
                    cadena+=caracter
            else:
                novalidos.append([caracter,reglon])
            if indice==len(linea)-1:
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                elif constructor_numero!="":
                    numeros_lista.append(["NUMERO",constructor_numero,constructor_numero,reglon+1])
                elif constructor_operador!="":
                    operadores_lista.append([constructor_operador,reglon+1])
                else:
                    pass


  

                
print((Fore.BLUE+"INSTITUTO POLITECNICO NACIONAL").center(50," "))
print((Fore.BLUE+"ESCUELA SUPERIOR DE COMPUTO").center(50," "))
print((Fore.RED+"COMPILADORES").center(50," "))
print((Fore.GREEN+ Style.BRIGHT+ "   SELU V1.1   ").center(50," "))

data=[["IDENTIFICADOR","LEXEMA","LITERAL","LINEA"]]
print(Fore.BLUE + "{:{width}} {:{width}} {:{width}} {:{width}}".format(data[0][0], data[0][1],data[0][2],data[0][3], width=col_width) + Style.RESET_ALL)
print("-" *  4)

lectura(open("codigo.txt"))
escritura(palabras)
escritura(numeros_lista)
escritura(seperacion(operadores_lista))

    
    
for row in data[1:]:
    print(Fore.GREEN+"{:{width}}".format(row[0],width=col_width),Fore.WHITE+ "{:{width}} {:{width}} {:{width}}".format(row[1],row[2], row[3], width=col_width-1))