letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numeros=["0","1","2","3","4","5","6","7","8","9",]
#operadores=["+","-","/","*","=","<",">","<=",">=","==","(",")","{","}",",",".",";","//","/*","*/","!=","!"]
tokens=["y":"Y",
"clase":"CLASE",
"ademas":"ADEMAS",
"falso":"FALSO",
"para":"PARA",
"fun":"FUN",
"si":"SI",
"nulo":"NULO",
"o":"O",
"imprimir":"IMPRIMIR",
"retornar":"RETORNAR",
"super":"SUPER",
"este":"ESTE",
"verdadero":"VERDADERO",
"var":"VAR",
"mientras":"MIENTRAS",
"identificador":"IDENTIFICADOR",
"cadena":"CADENA",
"numero":"NUMERO",
"(":"PAR ABRE",
")":"PAR CIERRA",
"{":"LLAVE ABRE",
"}":"LLAVE CIERRA",
",":"COMA",
".":"PUNTO",
";":"PUNTOYCOMA",
"-":"MENOS",
"+":"MAS",
"*":"MULT",
"/":"DIVISION",
"!":"NEGACION",
"!=":"NOESIGUAL",
"=":"ASIGNACION",
"==":"IGUAL",
"<":"MENOR",
"<=":"MENOROIGUAL",
">":"MAYOR",
">=":"MAYOROIGUAL",
"//":"COMENTARIO",
"/*":"COMENTARIO",
"*/":"COMENTARIO",
"1":"NUMERO",
"2":"NUMERO",
"3":"NUMERO",
"4":"NUMERO",
"5":"NUMERO",
"6":"NUMERO",
"7":"NUMERO",
"8":"NUMERO",
"9":"NUMERO",
"0":"NUMERO"]
operadores=["+","-","/","*","="]
def estado_0(caracter):
    caracter=caracter
    if caracter==" ":
        return
    if caracter in letras:
        estado_palabras(caracter)
        

def estado_palabras(caracter):
    caracter=caracter
    palabra=[]
    palabra.append(caracter)
    
    

archivo=open("codigo.txt","r")
col_width=20
i=0
palabras=[]
for linea in archivo:
    i+=1
    for caracter in linea:
        estado_0(caracter)





