#!python

# listbox#1.py

# description: listbox exercise
# author: arataca89@gmail.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# global vars ###################################
start = 0

#################################################


# functions #####################################
def add_function():
    if entry.get() != '':
        listbox.insert('end', entry.get())
    entry.delete(0,'end')


def del_function():
    item_index = listbox.curselection() # pega o indice do item / takes the item's index
    if item_index != (): # curselection() retorna uma tupla / curselection() returns a tuple
        listbox.delete(item_index)


def search_function():
    global start
    
    string = entry.get()
    size = listbox.size() # pega o numero de linhas / takes the number of lines    
    listbox.select_clear(0,'end')
    
    for item in range(start, size):
        if listbox.get(item).find(string) != -1:
            listbox.selection_set(item)
            #print(listbox.get(item)) 
            start += 1  
            return            
        else:
            start += 1
        #    print('nao tem este item')        
    

def itemSelected_function(event):
    global start
    start = listbox.curselection()
    if start != ():
        start = int(start[0])
        print(start)

    
#################################################


# GUI ###########################################
window = Tk()
window.resizable(0,0)
window.title('Listbox')


listbox = Listbox(window, width=20, height=7)
listbox.bind('<<ListboxSelect>>',itemSelected_function)


frame = ttk.Frame(window, borderwidth = 3)


entry = ttk.Entry(frame)


buttonAdd = ttk.Button(frame, text='Adicionar / Insert', command=add_function)


buttonSearch = ttk.Button(frame, text='Pesquisar / Search', command=search_function)


buttonDel = ttk.Button(frame, text='Excluir / Delete', command=del_function)


##################################################


# grid ###########################################
listbox.grid(row=0, column=0, rowspan=4)
frame.grid(row=0, column=1, sticky='n')
entry.grid(sticky='ns')
buttonAdd.grid(sticky='we')
buttonSearch.grid(sticky='we')
buttonDel.grid(sticky='we')
#################################################


window.mainloop()

# fim / end
