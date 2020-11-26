# Definicion de clase Pizza para almacenar la informacion referente a cada Pizza

from typing import List
from canvas import msjBuild


class Pizza: 
    ingPrice = {
        'Jamon' : 40 ,
        'Champiñones' : 35 ,
        'Pimentones' : 30 ,
        'Doble Queso' : 40 ,
        'Aceitunas' : 57.5 ,
        'Pepperoni' : 38.5 ,
        'Salchichon' : 62.5
    }

    sizePrice = {
        'Grande' : 580 ,
        'Mediana' : 430 ,
        'Personal' : 280
    }

    def __init__(self, size: str = None , tops: List = None , nro: int = 0 , total: float = 0):
        self.size = size
        self.tops = tops
        self.nro = nro
        self.total = total

        self.priceSet()
    
# Funcion PriceSet para el calculo del precio total por la Pizza en funcion del
#  Tamaño y los ingredientes agregados.

    def priceSet(self):

        self.total += self.sizePrice[self.size]
        
        for i in range(0 , len(self.tops)):
            self.total += self.ingPrice[self.tops[i]]

# Funcion subTotal, Muestra el subtotal por la Pizza.

    def subtotal(self):
        baseStr = "SubTotal por una Pizza " + self.size + ': ' + str(self.total)
        print(baseStr + '\n') 

    def __str__(self) -> str:
        pizzStr = msjBuild(self.size , self.tops)
        pizzStr += '\n ---> Costo Pizza ' + str(self.size) + ' ----- ' + str(self.sizePrice[self.size])
        #print('\n ---> Costo Pizza ' , self.size , ' ----- ' , str(self.sizePrice[self.size]))

        if(len(self.tops) != 0):
            #print('\n ---> Ingredientes Adicionales')

            pizzStr += '\n ---> Ingredientes Adicionales'

            for i in range(0 , len(self.tops)):
                #print('\n ------> ' , self.tops[i] , ' ------ ' , str(self.ingPrice[self.tops[i]]))
                pizzStr += '\n ------> ' + str(self.tops[i]) + ' ------ ' + str(self.ingPrice[self.tops[i]])
        
        #print('\n ---> Subtotal de la Pizza ---- ' , str(self.total))
        pizzStr += '\n ---> Subtotal de la Pizza ---- ' + str(self.total)
        return pizzStr



        



    