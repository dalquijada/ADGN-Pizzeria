# Clase Receipt - Recibo para la creacion de recibos guardados en Archivos
# Extra - #1

from order import Order


class Receipt:

    def __init__(self , rec_Order: Order = None):
        self.rec_Order = rec_Order

# Funcion printReceipt, se encarga de guardar el recibo final de la orden en un archivo.

    def printReceipt(orders: Order ):
        filename = 'recibo' + '.txt'

        with open(filename , 'w') as receipt:
            receipt.write(str(orders))
                
            receipt.close()
