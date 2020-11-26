# Proyecto 1 - Electiva Programacion en Python
# Elaborado por:
# Adrian Luces
# Daniel Lopez
# Giovanni Alcala
# Nestor Angeles

from receipt import Receipt
from order import Order
from pizza import Pizza
from canvas import menuTitle, msjBuild, sizes, titulo, toppings

# Constantes empleadas para realizar validacion de entradas

AFFIRM = ['s'  ,'S']
NEGA = ['n' , 'N']

menuLoop = True
pNro = 1
currentOrder = Order()

# Funcion takeOrder
# Comprende el Loop mediante el cual se ordenan las pizzas y sus condimentos

def takeOrder(pNro):
    orderLoop = True
    

    while(orderLoop):
        titulo(pNro)
        size = sizes()
        tps = toppings()

        pizza = Pizza(size , tps , pNro)
        print(msjBuild(size , tps))
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
            pNro += 1
            currentOrder.pizzas.append(pizza)

            print('\nEl pedido tiene un total de ' , pNro , ' Pizza(s) por un monto de: ' , str(currentOrder.orderTotal) + '\n')
            print('Gracias por su Compra vuelva pronto !!! \n')

            currentOrder.printOrder()

            orderLoop = False

            break
    
#Funcion Main

if __name__ == "__main__":

# Loop del Menu principal de la aplicacion

    while(menuLoop):
        
        menuTitle()
        resp = input('\n---> Eleccion: ')

# Opciones 

        if(resp not in ['1','2','3']):
            print('\n Seleccione una opcion Valida \n')

        elif(resp == '1'):
            takeOrder(pNro)

        elif(resp == '2'):
            if(len(currentOrder.pizzas) != 0):
                print('\n Imprimiendo recibos de las ultimas ordenes !')
                Receipt.printReceipt(str(currentOrder))
            else:
                print('\n No ha realizado ninguna orden todavia :(')

        elif(resp == '3'):
            menuLoop = False

            print('Gracias por usar la App de Pizzeria UCAB hasta pronto ! (U w U)\n')
            break
