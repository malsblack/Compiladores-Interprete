import json
tokens=json.load(open("tokens.json"))
palabras_reservadas=tokens["Palabas_reservadas"]
numeros=tokens["Numeros"]
operadores=tokens["Operadores"]
palabras=[]
numeros_lista=[]  
operadores_lista=[]
novalidos=[]


def lectura(archivo):
    for reglon,linea in enumerate(archivo):

        palabra="" 
        constructor_numero=""  
        constructor_operador=""
        cadena=""
        comentario=""
        
        for indice,caracter in enumerate(linea):
            if caracter.isalpha(): #Validacion letras
                palabra+=caracter
                if constructor_operador!="":
                    operadores_lista.append([constructor_operador,reglon+1])
                    constructor_operador=""

                    

            elif caracter in numeros: #Validacion numeros
                if palabra !="":
                    palabra+=caracter
                else:
                    constructor_numero+=caracter
                    
                if constructor_operador!="":
                    operadores_lista.append([constructor_operador,reglon+1])
                    constructor_operador=""

            elif caracter in operadores: #validacion operadores
                
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    numeros_lista.append([constructor_numero,reglon+1])
                    constructor_numero=""
                if constructor_operador!="":
                    constructor_operador+=caracter
                else:
                    constructor_operador+=caracter
            elif caracter=='"' or caracter=="'":
                palabra+=caracter

                
                    
            elif caracter ==" ":
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    numeros_lista.append([constructor_numero,reglon+1])
                    constructor_numero=""
                    
            elif caracter=='"':
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                    palabra=""
                if constructor_numero!="":
                    numeros_lista.append([constructor_numero,reglon+1])
                    constructor_numero=""
                palabra+=caracter
                
                if '"' in palabra:
                    palabra+=caracter
                    palabras.append(palabra)
                    palabra=""
                    
                    
                    
            else:
                novalidos.append([caracter,reglon])
            if indice==len(linea)-1:
                if palabra!="":
                    palabras.append([palabra,reglon+1])
                elif constructor_numero!="":
                    numeros_lista.append([constructor_numero,reglon+1])
                elif constructor_operador!="":
                    operadores_lista.append([constructor_operador,reglon+1])
                else:
                    pass
    print(palabras)
    print(numeros_lista)
    print(operadores_lista)
  

                
            
    
lectura(open("codigo.txt"))
