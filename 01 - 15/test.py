"""
1. Si listamos todos los números por debajo del 10 que son múltiplos de 3 o 5 obtenemos: 3, 5, 6 y 9. La suma de estos múltiplos es 23. Realice un algoritmo para encontrar la suma de todos los múltiplos de 3 y 5 por debajo de 1000.
"""
num = 0
for n in range(1, 1001):
    if n % 3 == 0 and n % 5 == 0:
        num += n

print(num)


"""
2. Escriba una rutina que imprima los números del 1 al 100 pero: cuando el número sea múltiplo de 3, 
imprima “Tic”, en lugar del número. Cuando el número sea múltiplo de 5, imprima “Toc”, en lugar del número. 
Cuando el número sea múltiplo tanto de 3 como de 5, imprima “TicToc”, en lugar del número.
"""

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("TicToc")
    elif n % 3 == 0:
        print("Tic")
    elif n % 5 == 0:
        print("Toc")
    else:
        print(n)


"""
3. Escribe el código para generar un objeto en que las keys (claves) sean los nombres de los depósitos y los valores un arreglo con los números de serie de los productos ordenados alfabéticamente por nombre."""

"""
4. Haga un programa que filtre el arreglo y devuelva un arreglo con solo el nombre de sus amigos. Si un nombre tiene exactamente 4 letras, ¡puedes estar seguro que es amigo tuyo! De lo contrario, puede estar seguro de que no…"""

#Amigo = [“Ryan”, “Kieran”, “Mark”, “Miguel”]  Deberia [“Ryan”, “Mark”]

"""
5. Escribe una función llamada sumaDigitos que retorne la suma de todos los dígitos de un número dado, por ejemplo:
5646 => 5+6+4+6 => 21
"""