#ABECEDARIOS

abecedario_letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
abecedario_numeros=["0","1","2","3","4","5","6","7","8","9"]
abecedario_operadores=["+","-","/","*","="]
#operadores=["+","-","/","*","=","<",">","<=",">=","==","(",")","{","}",",",".",";","//","/*","*/","!=","!"]

#----------------------------------------------------------------------------------------------------------------------------
#TOKENS

tokens={"y":"Y","clase":"CLASE","ademas":"ADEMAS","falso":"FALSO","para":"PARA","fun":"FUN","si":"SI","nulo":"NULO","o":"O","imprimir":"IMPRIMIR","retornar":"RETORNAR","super":"SUPER","este":"ESTE","verdadero":"VERDADERO","var":"VAR","mientras":"MIENTRAS","identificador":"IDENTIFICADOR","cadena":"CADENA","numero":"NUMERO","(":"PAR ABRE",")":"PAR CIERRA","{":"LLAVE ABRE","}":"LLAVE CIERRA",",":"COMA",".":"PUNTO",";":"PUNTOYCOMA","-":"MENOS","+":"MAS","*":"MULT","/":"DIVISION","!":"NEGACION","!=":"NOESIGUAL","=":"ASIGNACION","==":"IGUAL","<":"MENOR","<=":"MENOROIGUAL",">":"MAYOR",">=":"MAYOROIGUAL","//":"COMENTARIO","/*":"COMENTARIO","*/":"COMENTARIO","1":"NUMERO","2":"NUMERO","3":"NUMERO","4":"NUMERO","5":"NUMERO","6":"NUMERO","7":"NUMERO","8":"NUMERO","9":"NUMERO","0":"NUMERO"}
#---------------------------------------------------------------------------------------------------------------------------

#VARIIABLES GLOBALES

datos=[]  
aux=[] 
#-----------------------------------------------------------------------------------------------------------------------------
#FUNCIONES

def estado_0(datos):
    datos=datos
    for palabra in datos:
        for caracter in palabra[0]:
            aux.append(caracter)
        for caracter in aux:
            if caracter in abecedario_letras and aux[aux.index(caracter)+1] in abecedario_letras:
                print(f"soy soy letra: {caracter}")
            else:
                print(f"{caracter}")

                
        




archivo=open("codigo.txt","r")
i=0
for linea in archivo:
    i+=1
    datos.append([linea.strip('\n').lower(),i])
estado_0(datos)






