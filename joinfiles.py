#!python
#-*- coding:utf-8 -*-

# joinfiles.py

import sys
from datetime import datetime


def to_join():
    '''Junta todos os arquivos passados como argumento na linha de comando.'''
    joinedfiles = ''
    separator = 30 * '='
    for filename in sys.argv[1:]:
        print(filename)
        with open(filename,'r',encoding='utf-8') as arquivo:
            joinedfiles += separator + '\n' + filename + '\n' + \
            separator + '\n' + arquivo.read() + '\n\n\n'            

    name = 'joinfiles_' + str(datetime.now()) + '.txt'
    name = name.replace(' ','_')
    name = name.replace('-','_')
    name = name.replace(':','_')
    
    with open(name,'w',encoding='utf-8') as arquivo:
        arquivo.write(joinedfiles)

    print('Arquivos juntos em :' + name)
    

if __name__ == '__main__':
    to_join()
    
		
