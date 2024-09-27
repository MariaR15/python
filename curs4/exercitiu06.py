lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

a = len(lista_start)
lista_1 = []
lista_2 = []
lista_3 = []

for i in range(a):
    if i % n == 0:
        lista_1.append(lista_start[i])

        if i % n - 1 == 0:
            lista_2.append(lista_start[i])

            if i % n - 1 == 0:
                lista_3.append(lista_start[i])

    print(lista_1, lista_2, lista_3)
