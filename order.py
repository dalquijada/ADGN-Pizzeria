# Definicion Clase Order para almacenamiento de la Orden actual.

from pizza import Pizza
from typing import List


class Order:
    def __init__(self, orderId:str = None , pizzas: List = [] , orderTotal: float = 0):
        self.orderId = orderId
        self.pizzas = pizzas
        self.orderTotal = orderTotal

# Funcion addSubTotal, se encarga de actualizar el costo total de la orden en funcion
# de los costos de cada Pizza ordenada

    def addsubTotal(self , subtotal):
        self.orderTotal += subtotal

# Funcion printOrder, se encarga de mostrar en pantalla la orden final.

    def printOrder(self):
        print(' -----Recibo----- ')

        print('\n ID de la Orden: ' , self.orderId )

        for i in range(0 , len(self.pizzas)):
            print('\n<--------------------------------------------------->\n')
            print(self.pizzas[i])
        
        print('\n Total de la orden: ------- ' , str(self.orderTotal))


    def __str__(self) -> str:
        ordStr = ' -----Recibo----- \n'
        ordStr += '\n ID de la Orden: ' + str(self.orderId) + '\n'

        for i in range(0 , len(self.pizzas)):
            ordStr += '\n<--------------------------------------------------->\n'
            ordStr += str(self.pizzas[i])
        
        ordStr += '\n Total de la orden: ------- ' + str(self.orderTotal)
        return ordStr + '\n'



