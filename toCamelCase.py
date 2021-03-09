#!/usr/bin/env python

# arataca89@gmail.com

# CodeWars exercise:

# Complete the method/function so that it converts dash/underscore
# delimited words into camel casing. The first word within the output
# should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    buff = ""
    for i in range(len(text)):        
        if (text[i-1] == '-' or text[i-1] == '_'):     
           buff += text[i].upper() 
        else:
           buff += text[i]
    
    output = ""
    for i in range(len(buff)):                    
        if (buff[i] == '-' or buff[i] == '_'):        
           pass           
        else:
           output += buff[i]    
    
    return(output)


print(to_camel_case("to-camel_case"))
print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))


