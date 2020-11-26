# Proyecto 1 - Electiva Programacion en Python
# Elaborado por:
# Adrian Luces
# Daniel Lopez
# Giovanni Alcala
# Nestor Angeles

from order import Order
from pizza import Pizza
from canvas import msjBuild, sizes, titulo, toppings

AFFIRM = ['s'  ,'S']
NEGA = ['n' , 'N']

menuLoop = True
orderLoop = True
pNro = 1


if __name__ == "__main__":

    currentOrder = Order()

    while(orderLoop):
        titulo(pNro)
        size = sizes()
        tps = toppings()

        pizza = Pizza(size , tps , pNro)
        msjBuild(size , tps)
        pizza.subtotal()
        currentOrder.addsubTotal(pizza.total)
        resp = input('¿Desea Continuar?(s/n) : ')

        if((resp not in AFFIRM) and (resp not in NEGA)):
            print('Eleccion Invalida...')

            while((resp not in AFFIRM) and (resp not in NEGA)):
                resp = input('¿Desea Continuar?(s/n) : ')

                if((resp not in AFFIRM) and (resp not in NEGA)):
                    print('Eleccion Invalida...')
                else:
                    break
        
        if(resp in AFFIRM):
            pNro += 1
            currentOrder.pizzas.append(pizza)
        else:
            print('\nEl pedido tiene un total de ' , pNro , ' Pizza(s) por un monto de: ' , str(currentOrder.orderTotal) + '\n')
            print('Gracias por su Compra vuelva pronto !!! \n')
            orderLoop = False
            break


                
