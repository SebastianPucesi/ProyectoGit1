#for i in range (5):
#    print(i, end=" ,")
'''
#Metodo recursivo
def MostrarNumero(numero):
    #Caso base
    if numero <=0:
        return
    #Caso recursivo
    else:
        print(numero, end=" ,")
        return MostrarNumero(numero-1)

MostrarNumero(6)'''

def totalPaginas(Libros):
    if len(Libros) == 1:
        return Libros [0]
    else:
        return Libros[0] + totalPaginas(Libros[1:])
print(totalPaginas([10,20,30,40]))