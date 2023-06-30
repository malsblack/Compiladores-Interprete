import json
reglas=json.load(open("validaciones.json"))

def entrada_analizador(lista):
    diccionario_sublistas={}
    for DECLARATION in lista[1:]:
        ultimo=DECLARATION[-1]
        if ultimo not in diccionario_sublistas:
            diccionario_sublistas[ultimo] = []
            diccionario_sublistas[ultimo].append(DECLARATION)
        else:
            diccionario_sublistas[ultimo].append(DECLARATION)
    return diccionario_sublistas

def analizar(cadena,simbolo,reglas):
    if simbolo in reglas:
        for produccion in reglas[simbolo]:
            if cadena[0]==produccion:
                cadena.pop(cadena[0])
                if analizar(cadena,cadena[0],reglas):
                    return True
    elif simbolo=="TERMINAL":
        if cadena:
            return False
    return False

    
def proceso_analizador(datos):
    for linea in datos:
        cadena=[]
        for tokens in datos[linea]:
            cadena.append(tokens[0])
            
        if analizar(cadena,"DECLARATION",reglas):
            pass
        else:
            print("Error de sintaxis en la linea ")
        
            
    
def analizador_sintactico(lista):
    datos=entrada_analizador(lista)
    proceso_analizador(datos)
    