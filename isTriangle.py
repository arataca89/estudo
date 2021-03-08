#!/usr/bin/env python

# arataca89@gmail.complex

# CodeWars exercise:
# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built
# with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

# Para construir um triângulo não podemos utilizar qualquer medida,
# tem que seguir a condição de existência:
# Para construir um triângulo é necessário que a medida de qualquer
# um dos lados seja menor que a soma das medidas dos outros dois e
# maior que o valor absoluto da diferença entre essas medidas.
#
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
#
# Referência: https://brasilescola.uol.com.br/matematica/triangulo.htm


def is_triangle(a, b, c):

    if( a<=0 or b<=0 or c<=0):
        return False
    
    if( (abs(b - c ) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) ):
        return True
    else:
        return False


print( is_triangle(1, 2, 2), "True" )
print( is_triangle(7, 2, 2), "False")
print( is_triangle(1, 2, 3), "False")
print( is_triangle(1, 3, 2), "False")
print( is_triangle(3, 1, 2), "False")
print( is_triangle(5, 1, 2), "False")
print( is_triangle(1, 2, 5), "False")
print( is_triangle(2, 5, 1), "False")
print( is_triangle(4, 2, 3), "True")
print( is_triangle(5, 1, 5), "True")
print( is_triangle(2, 2, 2), "True")
print( is_triangle(-1, 2, 3), "False")
print( is_triangle(1, -2, 3), "False")
print( is_triangle(1, 2, -3), "False")
print( is_triangle(0, 2, 3), "False")
