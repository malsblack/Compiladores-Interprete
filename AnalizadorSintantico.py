def analizador_sintantico(lista):
    VAR_DECL=[]
    diccionario_sublistas={}
    for DECLARATION in lista[1:]:
        ultimo=DECLARATION[-1]
        if ultimo not in diccionario_sublistas:
            diccionario_sublistas[ultimo] = []
            diccionario_sublistas[ultimo].append(DECLARATION)
        else:
            diccionario_sublistas[ultimo].append(DECLARATION)
    for elemento in diccionario_sublistas:
        print(f"{diccionario_sublistas[elemento]} \n")