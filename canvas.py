# Base de la App

import os
from typing import List

def titulo(nro:int):
    print('\n******************************\n' + '*       Pizzeria Ucab !!!    *\n' + '******************************\n' )
    print('--> Pizza Numero ' , nro , '<-- \n')


def sizes():
    allowed = ['p' , 'P' , 'm' , 'M' , 'g' , 'G']

    print('\n Opciones: \n')
    print(' => Personal (p)\n => Mediana  (m)\n => Grande   (g)\n')
    selected = input(' => Eleccion: ')

    if(selected not in allowed):
        print('\nElige un Tamaño Valido !\n')
        while(selected not in allowed):
            print(' => Personal (p)\n => Mediana (m)\n => Grande (g)\n')
            selected = input(' => Eleccion: ')
    
    if(str.lower(selected) == 'p'):
        print('Tamaño Seleccionado: Personal')
        return 'Personal'

    elif(str.lower(selected) == 'm'):
        print('Tamaño Seleccionado: Mediana')
        return 'Mediana'

    elif(str.lower(selected) == 'g'):
        print('Tamaño Seleccionado: Grande')
        return 'Grande'

def toppings():
    allowed = ['ja' , 'ch' , 'pi' , 'dq' , 'ac' , 'pp' , 'sa']

    ing = {
        'ja' : 'Jamon' ,
        'ch' : 'Champiñones' ,
        'pi' : 'Pimentones' ,
        'dq' : 'Doble Queso' ,
        'ac' : 'Aceitunas' ,
        'pp' : 'Pepperoni' ,
        'sa' : 'Salchichon'
    }

    tops = []
    ready = False

    print('\n Ingredientes Disponibles: \n')

    print(
        ' --> Jamon        (ja)\n' ,
        '--> Champiñones  (ch)\n' ,
        '--> Pimenton     (pi)\n' ,
        '--> Doble Queso  (dq)\n' ,
        '--> Aceitunas    (ac)\n' ,
        '--> Pepperoni    (pp)\n' ,
        '--> Salchichon   (sa)\n'
    )

    while(not ready):

        selected = input('Seleccione ingredientes a agregar(ENTER para terminar): ')

        if(selected in ing.keys()):
            if(ing[selected] not in tops ):
                tops.append(ing[selected])
            else:
                print('\n El ingrediente ya se encuentra seleccionado !\n')
        elif(len(selected) == 0):
            ready = True
            break
        else:
            print('\nIngrediente invalido... \n')



    return tops

def msjBuild(size: str , tops: List):
    if(len(tops) == 0):
        baseStr = "\nUsted Selecciono una Pizza " + size + " Margarita."
    else:
        baseStr = "\nUsted Selecciono una Pizza " + size + " Con "
        for i in range(0 , len(tops)):
            if(i == len(tops) - 1):
                baseStr += ' ' + tops[i] + '.'
            else:
                baseStr += ' ' + tops[i] + ','

    print(baseStr)
