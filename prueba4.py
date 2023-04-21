import json
#Importacion de tokens
tokens=json.load(open("tokens.json","r"))
palabras_reservadas=tokens["Palabas_reservadas"]
numeros=tokens["Numeros"]
operadores=tokens["Operadores"]
letras=tokens["Letras"]
espacio=" "
palabra=[]

estados={'0','1'}
transiciones={'0':'0',
              '0':'1',
              '1':'0'}

def procesar(linea):
    for caracter in linea:
        estado='0'
        if caracter in espacio:
            estado='0'
            pass
        elif caracter in letras:
            estado='1'
            
        
        

def leer(archivo):
    lista=[]
    for linea in archivo:
        lista.append(linea[:-1])
    lista.pop(len(lista)-1)
    lista.append(linea)
    return lista
    

procesar(leer(open("codigo.txt","r")))