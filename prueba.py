#ABECEDARIOS

abecedario_letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abecedario_numeros=["0","1","2","3","4","5","6","7","8","9"]
abecedario_operadores=["+","-","/","*","="]
#operadores=["+","-","/","*","=","<",">","<=",">=","==","(",")","{","}",",",".",";","//","/*","*/","!=","!"]

#----------------------------------------------------------------------------------------------------------------------------
#TOKENS

tokens={"y":"Y","clase":"CLASE","ademas":"ADEMAS","falso":"FALSO","para":"PARA","fun":"FUN","si":"SI","nulo":"NULO","o":"O","imprimir":"IMPRIMIR","retornar":"RETORNAR","super":"SUPER","este":"ESTE","verdadero":"VERDADERO","var":"VAR","mientras":"MIENTRAS","identificador":"IDENTIFICADOR","cadena":"CADENA","numero":"NUMERO","(":"PAR ABRE",")":"PAR CIERRA","{":"LLAVE ABRE","}":"LLAVE CIERRA",",":"COMA",".":"PUNTO",";":"PUNTOYCOMA","-":"MENOS","+":"MAS","*":"MULT","/":"DIVISION","!":"NEGACION","!=":"NOESIGUAL","=":"ASIGNACION","==":"IGUAL","<":"MENOR","<=":"MENOROIGUAL",">":"MAYOR",">=":"MAYOROIGUAL","//":"COMENTARIO","/*":"COMENTARIO","*/":"COMENTARIO","1":"NUMERO","2":"NUMERO","3":"NUMERO","4":"NUMERO","5":"NUMERO","6":"NUMERO","7":"NUMERO","8":"NUMERO","9":"NUMERO","0":"NUMERO"}
#---------------------------------------------------------------------------------------------------------------------------

#ESTADOS
estado_inicial = "inicial"
estado_numero = "número"
estado_palabra = "palabra"
estado_operador = "operador"
error = "error"
estado_final = {estado_numero, estado_palabra, estado_operador}

datos=[]  
aux=[] 
lista=[]
#-----------------------------------------------------------------------------------------------------------------------------
#FUNCIONES

def transition(estado, simbolo):
    if estado == estado_inicial:
        if simbolo in abecedario_numeros:
            return estado_numero
        elif simbolo in abecedario_letras:
            return estado_palabra
        elif simbolo in abecedario_operadores:
            return estado_operador
        else:
            return error
    elif estado == estado_numero:
        if simbolo in abecedario_numeros:
            return estado_numero
        else:
            return estado_final.intersection({estado_numero}).pop()
    elif estado == estado_palabra:
        if simbolo in abecedario_letras or simbolo in a:
            return estado_palabra
        else:
            return estado_final.intersection({estado_palabra}).pop()
    elif estado == estado_operador:
        return estado_final.intersection({estado_operador}).pop()
    else:
        return error

def analizador(input_string,i):
    estado = estado_inicial
    lexema = ""
    token = ""
    for simbolo in input_string:
        nuevo_estado = transition(estado, simbolo)
        lexema += simbolo
        if nuevo_estado == error:
            return "Error: símbolo no válido"
        elif nuevo_estado in estado_final:
            if nuevo_estado=="palabra":
                lista.append([nuevo_estado,lexema,"STRING",i])
                pass
            elif nuevo_estado=="número":
                lista.append([nuevo_estado,lexema,"INT",i])
                pass
            else:
                lista.append([nuevo_estado,lexema,"",i])
                pass
                
                

def lectura_datos(datos):
    datos=datos
    for palabra in datos:
        for caracter in palabra[0]:
            aux.append(caracter)
        for caracter in aux:
            analizador(caracter,i=palabra[1])
                

                
        




archivo=open("codigo.txt","r")
i=0
for linea in archivo:
    i+=1
    datos.append([linea.strip('\n').lower(),i])
lectura_datos(datos)
print(lista)






