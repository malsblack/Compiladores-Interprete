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

def analizar(lista,simbolo):
    pila=["DECLARATION"]
    for elemento in lista:
        if elemento == pila[0]:
            pila.pop(pila[0])
            pass
        elif elemento in reglas[pila[0]]:
            pila.append(reglas[pila[0]])
            pila.pop(0)
        print(pila)

    
def proceso_analizador(datos):
    for linea in datos:
        cadena=[]
        for tokens in datos[linea]:
            cadena.append(tokens[0])
        analizar(cadena,"DECLARATION")
        
            
    
def analizador_sintactico(lista):
    datos=entrada_analizador(lista)
    proceso_analizador(datos)
    