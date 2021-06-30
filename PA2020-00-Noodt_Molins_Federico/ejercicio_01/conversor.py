items = []
precios = []

def conversor(items, precios):
    imprenta = open('sales_imprenta.txt', 'r')

    lineas = imprenta.read()


    lineas = lineas.replace('\n', ',')
    precioItems = lineas.split(',')

    for i in range(0, len(precioItems)):
        if i %2 == 0:
            items.append(precioItems[i])
        elif i %2 != 0:
            precios.append(float(precioItems[i]))

    imprenta.close()

    return items, precios

conversor(items,precios)

Items = items
Precios = precios
