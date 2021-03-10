#!/usr/bin/env python

# arataca89@gmail.com 

# CodeWars exercise:

# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer
# that is the square of an integer; in other words, it is the
# product of some integer with itself.

# The tests will always use some integral number, so don't worry
# about that in dynamic typed languages.

# Examples
# -1  =>  false
# 0  =>  true
# 3  =>  false
# 4  =>  true
# 25  =>  true
# 26  =>  false

import math

def is_square(n):
    if(n < 0):
        return False
        
    raiz = math.sqrt(n)
    inteiro = math.floor(raiz)
    
    #print(raiz)
    #print(inteiro)
    
    #print(n)
    #print(inteiro*inteiro)
    
    if(n == (inteiro*inteiro)):
        return True
    else:
        return False
    

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))
