#Ejercicio de arreglos de 1 hasta n
#Saber cuales son primos(?)

import sys

num=int(sys.argv[1])
#num = int(input("ingrese número: "))

def mi_arregloFC(num):
    lista=[]
    for i in range(1,num+1):
        lista.append(i)
        
    return print(lista)

def regios(num):
    lista=[]
    for i in range(2, num + 1):
        primos = True
        for j in range(2,i):
            if i == j:
               break
            elif i%j == 0:
               primos = False
            else:
               continue
        if primos == True:
            lista.append(i)
            
    return print(lista)
    
mi_arregloFC(num)
regios(num)
    