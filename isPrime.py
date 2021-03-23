#####################################################################

# arataca89@gmail.com

# 20210323

# Um número é primo se ele somente for divisível por ele mesmo e por 1

# este algoritmo calcula o resto das divisões sucessivas do número,
# dividindo o número por 2,3,4 ... até n - 1 

# cada resto é analisado ... se o resto for zero o número é divisível
# por algum outro número que não seja ele mesmo ou 1, logo não será
# primo e a função retorna zero

# se as divisões sucessivas ocorrerem até o divisor chegar a n - 1
# o número só será divisível por ele mesmo ou por 1, logo será
# um número primo e a função retornará 1

def primo(nr):

    divisor = 2
    
    while(divisor < nr):
        print()
        print("nr : ",nr," ; divisor: ",divisor)
        print("nr / divisor =",nr//divisor," ; resto: ",nr % divisor)
        if(nr % divisor == 0):
            print()
            return False;
        else:
            divisor += 1
    print() 
    return True
	

#print(primo(13))
print(primo(15))

	
