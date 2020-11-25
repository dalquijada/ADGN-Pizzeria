# Definicion de clase Pizza

from typing import List


class Pizza:
    def __init__(self, size: str = None, tops: List = None, nro: int = 0, total: float = 0):
        self.size = size
        self.tops = tops
        self.nro = nro
        self.total = total

        self.priceSet()

    def priceSet(self):
        #Dict de ingredientes
        ingPrice = {
            'Jamon': 40,
            'Champiñones': 35,
            'Pimentones': 30,
            'Doble Queso': 40,
            'Aceitunas': 57.5,
            'Pepperoni': 38.5,
            'Salchichon': 62.5
        }
        #Dict de tamaños
        sizePrice = {
            'Grande': 580,
            'Mediana': 430,
            'Personal': 280
        }

        self.total += sizePrice[self.size]

        for i in range(0, len(self.tops)):
            self.total += ingPrice[self.tops[i]]

    def subtotal(self):
        baseStr = "SubTotal por una Pizza " + self.size + ': ' + str(self.total)
        print(baseStr + '\n')
