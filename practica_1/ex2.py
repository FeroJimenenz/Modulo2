#Ejercicio de arreglos de 1 hasta n
#Saber cuales son primos(?)

import sys

num=int(sys.argv[1])
#num = int(input("ingrese número: "))

def mi_arregloFC(num):
    lista=[]
    for i in range(num):
        lista.append(i+1)
        
    return print(lista)
    
def regios(num):
    lista=[]
    for n in range(1,num):
        if num % n == 0:
            lista.append(n)

    return print(lista)
    
mi_arregloFC(num)
regios(num)
    