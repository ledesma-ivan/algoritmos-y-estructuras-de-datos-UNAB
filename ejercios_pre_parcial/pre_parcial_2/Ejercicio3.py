'''
Escribir una función iterativa 
que calcule la suma de los primeros N números naturales.
Recibe como parámetro el número N. '''

def suma_hasta(n):
    if not isinstance(n, int):
        raise ValueError('El valor debe ser un numero entero.')
    if n < 0:
        raise ValueError('El numero no puede ser negativo')
    
    total = 0
    for i in range(n+1):
        total+=i
    return total


n = int(input('Hasta que numero, queres que suma: '))
resultado = suma_hasta(n)
print(resultado)