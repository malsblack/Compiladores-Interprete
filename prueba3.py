
patron_identificador = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
aux=[]
palabras=[]
def lector(palabra):
    for caracter in palabra:
        if caracter==None:
            pass
        if caracter in patron_identificador:
            aux.append(caracter)
        else:
            if len(aux)==0:
                pass
            else:
                palabras.append("".join(aux))
                aux.clear()
                print(palabras)
       

lista=[]
archivo=open("codigo.txt","r")
for linea in archivo:
    lista.append(linea[:-1])
    
lista.pop(len(lista)-1)
lista.append(linea)

for palabra in lista:
    lector(palabra)

