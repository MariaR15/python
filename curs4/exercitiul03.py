# Scrieti suma cu iteratie prin acestea
lista = [10, 13, 2, 6, 14]
suma = None

for i, element in enumerate(lista):
    print(i, element)
    if i != len(lista):
        suma = element + lista[i + 1]
    print(suma)
