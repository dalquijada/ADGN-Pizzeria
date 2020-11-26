# Base de la App
# El Modulo Canvas contiene estructuras empleadas en el flujo de
# la Aplicacion

import os
from typing import List

# Funcion Titulo , Muestra el titulo principal de la App

def titulo(nro:int):
    print('\n******************************\n' + '*       Pizzeria ADGN !!!    *\n' + '******************************\n' )
    print('--> Pizza Numero ' , nro , '<-- \n')


# Funcion Sizes, contiene el menu de eleccion de tamaños para las Pizzas

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


# Funcion Toppings, Comprende el menu de eleccion de Ingredientes o Toppings para agregar a la Pizza.

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

# Funcion msjBuild, se encarga de Crear los mensajes personalizados 
# en funcion de la pizza y los ingredientes seleccionados.

def msjBuild(size: str , tops: List) -> str:
    if(len(tops) == 0):
        baseStr = "\nUsted Selecciono una Pizza " + size + " Margarita."
    else:
        baseStr = "\nUsted Selecciono una Pizza " + size + " Con "
        for i in range(0 , len(tops)):
            if(i == len(tops) - 1):
                baseStr += ' ' + tops[i] + '.'
            else:
                baseStr += ' ' + tops[i] + ','
    
    #print(baseStr)
    return baseStr +'\n'


# Funcion menuTitle, se encarga de mostrar el menu principal de la aplicacion


def menuTitle():
    print('\n******************************\n' + '*       Pizzeria Ucab !!!    *\n' + '******************************\n' )

    print(
        '\n Bienvenidos a Pizzeria ADGN\n' +
        ' 1) Ordenar Pizzas\n' +
        ' 2) Imprimir Recibo de Orden\n' +
        ' 3) Salir\n' +
        '\n---> Escoja una opcion ingresando el numero de Opcion\n'

    )
       
