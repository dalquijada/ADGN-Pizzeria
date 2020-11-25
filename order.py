# Definicion Clase Order para almacenamiento de las distintas ordenes

from typing import List


class Order:
    def __init__(self, orderId: str = None, pizzas: List = [], orderTotal: float = 0):
        self.orderId = orderId
        self.pizzas = pizzas
        self.orderTotal = orderTotal

    def addsubTotal(self, subtotal):
        self.orderTotal += subtotal
