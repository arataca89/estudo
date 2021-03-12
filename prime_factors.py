#!/usr/bin/env python

# arataca89@gmail.com 

# CodeWars exercise:

# Given a positive number n > 1 find the prime factor decomposition
# of n. The result will be a string with the following form :

# "(p1**n1)(p2**n2)...(pk**nk)"
# where a ** b means a to the power of b

# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"


def primo(nr):
    divisor = 2	
   
    if (nr == 1):
        return 0			
    elif (nr == 2):
        return 1
    else:		
        while( divisor < nr):			
            if(nr % divisor == 0):
                return 0				
            else:
                divisor+=1
        return 1        
        
# end of primo()


def formata(lista):
    unicos = []
    string = ""
    #print(lista)
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    #print("unicos" + str(unicos))    
 
    for i in range(len(unicos)):
        string += "(" 
        string += str(unicos[i])
        if(lista.count(unicos[i]) > 1):
            string += ( "**" + str(lista.count(unicos[i])) + ")" )
        else:
            string += ")"
            
    return(string)
# end of formata()

        
def prime_factors(n):  
    nrs = []  
    aux = n;
    for i in range(2,n):
        if(primo(i)):
            while True:
                if(aux % i == 0):
                    if(aux == i):
                        nrs.append(i)
                        return(formata(nrs))
                    nrs.append(i)
                    aux = aux // i                    
                else:
                    break
            continue

# end of prime_factors()

s = prime_factors(86240)
print(s)
