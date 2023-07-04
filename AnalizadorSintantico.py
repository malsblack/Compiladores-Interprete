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
        for producciones in reglas[simbolo]:

            if producciones==cadena[0]:
                aux=cadena[0]
                cadena.pop(0)
                analizar(cadena,cadena[0],reglas[simbolo][aux])
            elif producciones=="TERMINAL":
                cadena.pop(0)
                analizar(cadena,cadena[0],reglas["VAR_INIT"])
                return True
            else:
                return True
            
                


    
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
    