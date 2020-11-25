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
