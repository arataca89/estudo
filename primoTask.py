#!/usr/bin/env python

# 20210320

#####################################################################
# Tarefa: verificar se um número pode ser escrito como a soma de
# quadrados de quatro números primos consecutivos ou não.
#
# O programa terá dois modos de operação: 
#
# modo 1: 
# - entrada: 5 números naturais n1,n2,n3,n4 e n
# - saída: "verdadeiro" se n pode ser escrito como a soma dos quadrados de
#   n1,n2,n3 e n4; "falso" caso contrário.
#
# modo 2:
# - entrada: um número natural n
# - saída: imprimir os quatro primos consecutivos cuja soma dos quadrados seja igual
#   a n ou imprimir "falso" caso não é possível representar n como a soma
#   dos quadrados de quatro números primos consecutivos.
#
# NÃO há necessidade de validar os dados de entrada

# TESTES
#
# modo 1: n1=2; n2=3; n3=4; n4=5; n=54 ==> True
# modo 1: n1=2; n2=3; n3=4; n4=5; n=53 ==> False
  

def primo(nr):

    divisor = 2
    
    while(divisor < nr):
        
        if(nr % divisor == 0):
            return False;
        else:
            divisor += 1
    return True


def modo1(n1,n2,n3,n4,n):

    if( int(n) == (int(n1)**2 + int(n2)**2 + int(n3)**2 + int(n4)**2) ):
        return True
    else:
        return False

    
def modo2(n):
    numeros = []
    primos = []
    
    for i in range(1, int(n)):
        if(primo(i)):
            numeros.append(i)
    
    #print(n)
    #print(numeros)
    
    for i in range(len(numeros)-3):

        produto = numeros[i]**2 + numeros[i+1]**2 + numeros[i+2]**2 + numeros[i+3]**2
        #print(produto)
        
        if(produto == int(n)):
            primos.append(numeros[i])
            primos.append(numeros[i+1])
            primos.append(numeros[i+2])
            primos.append(numeros[i+3])
    
    return primos
    

#####################################################################

# INICIO DO PROGRAMA
    
modo = input("Entre com o modo: ")

if (modo == "1"):

    n1 = input("Entre com n1: ")
    n2 = input("Entre com n2: ")
    n3 = input("Entre com n3: ")
    n4 = input("Entre com n4: ")
    n =  input("Entre com  n: ")
    
    if( modo1(n1,n2,n3,n4,n) ):
        print("verdadeiro")
    else:
        print("falso")
    
    
elif (modo == "2"):
    
    n = input("Entre com n: ")
    lista = modo2(n)
    
    if(len(lista) == 0):
        print("falso")
    else:
        print(lista)
 
