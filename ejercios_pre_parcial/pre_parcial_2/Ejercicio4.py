'''Escribir una función recursiva que 
calcule la suma de los primeros N números naturales. 
Recibe como parámetro el número N. 
'''

def suma_hasta(n):
    if not isinstance(n, int):
        raise ValueError('El valor debe ser un numero entero.')
    if n < 0:
        raise ValueError('El numero no puede ser negativo')
    
    if n == 1: # Caso base
        return 1
    else: # Recursion
        return n + suma_hasta(n-1)

print(suma_hasta(4))
