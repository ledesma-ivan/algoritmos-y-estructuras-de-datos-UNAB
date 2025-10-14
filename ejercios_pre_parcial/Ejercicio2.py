'''
Escribir una función que permita ordenar una Lista. 
Dicha función recibe 3 (tres) argumentos (lista, orden, copia), en donde, 
lista es la lista a ordenar, orden indica cómo se ordena la lista, 
puede ser ascendente o descendente, y 
copy es Verdadero cuando la función retornara una lista nueva. Por defecto,
la función nos devuelve una nueva lista ordenada de forma ascendente.
'''


def ordenar_lista(lista, orden='asc', copia=True):
    reverse = True if orden == 'desc' else False
    if copia == True:
        nueva_lista = sorted(lista, reverse=reverse)
        return nueva_lista
    else:
        lista.sort(reverse=reverse)
        return lista
