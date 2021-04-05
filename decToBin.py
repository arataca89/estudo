#!/usr/bin/env python
#####################################################################

# arataca89@gmail.com
# 20210405

# decToBin()
# Recebe um numero decimal e retorna uma lista com a representacao
# do decimal em numero binario.

# Exemplo:

# decToBin(15) retorna [1,1,1,1]


def decToBin(n):
    
    bin = []
    resto = n % 2
    quociente = 1
    
    while( quociente > 0 ):
        quociente = n // 2        
        resto = n % 2
        bin.append(resto)
        n = quociente
    
    bin.reverse()
    
    return bin
    

def testeDecToBin(lista):
    
    for i in lista:

        if(decToBin(i[0]) == i[1]):
            print("OK")
        else:
            print("ERRO")



listaTeste = [ (15,[1,1,1,1]),\
               (15,[1,1,1,0]),\
               (113,[1,1,1,0,0,0,1]),\
               (113,[0,1,1,0,0,0,1]),\
               (1,[1]) ]                


testeDecToBin(listaTeste)
# Saida esperada:
# (15,[1,1,1,1])        OK
# (15,[1,1,1,0])        ERRO
# (113,[1,1,1,0,0,0,1]) OK
# (113,[0,1,1,0,0,0,1]) ERRO
# (1,[1])               OK 

# fim de decToBin.py
