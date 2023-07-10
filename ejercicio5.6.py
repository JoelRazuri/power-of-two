"""
Potencias de dos.
    
    a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural,
    y devuelva True si el número es una potencia de 2, y False en caso contrario.
    
    b) Escribir una función que, dados dos números naturales pasados como parámetros,
    devuelva la suma de todas las potencias de 2 que hay en el rango formado por
    esos números (0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función
    es_potencia_de_dos, descripta en el punto anterior.
"""

def es_potencia_de_dos(natural):

    es_potencia=False

    for potencia in range(15):
        
        if natural==2**potencia:
            es_potencia=True

    return es_potencia

def suma_potencias_entre_dos_numeros(minimo,maximo):

    contador=0

    for natural in range(minimo,maximo+1):

        if es_potencia_de_dos(natural)==True:
            contador = contador + natural
        
    return contador

print(suma_potencias_entre_dos_numeros(1,10))