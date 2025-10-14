# Construir una lista por comprensión que contenga la siguiente serie de valores: 
# 1, 0, 1, 0, 1, 0, ...


# Ejemplo de lista por compresion 
# [expresión for elemento in iterable]

'''
En nuestro caso nos piden la siguiente serie de valores'''

n= int(input('Ingrese la cantidad de valores que quiera obtener: '))
lista = [1 if x % 2 == 0 else 0 for x in range(n)]

print(lista)