'''Escribir un algoritmo de busqueda binaria que reciba como entrada una estructura de datos cualquiera (cualquier tipo de colección de objetos,
 i.e array, lista, listas enlazadas, etc.) 
 y retorne el valor buscado, en caso contrario debe lanzar una excepción. '''


def busqueda_binaria(coleccion, valor_buscado):
    # Convertimos cualquier tipo de estructura de datos a una lista para poder trabajarla.
    elementos = list(coleccion)
    
    inicio = 0
    fin = len(elementos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        medio_valor = elementos[medio]

        if medio_valor == valor_buscado:
            return medio_valor

        if medio_valor < valor_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1

    raise ValueError("El valor no se encuentra en la colección")
