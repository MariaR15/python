######### if
nr1 = 4
# total = None
if nr1 < 4:
    total = nr1 + 1
elif nr1 < 2:
    total = nr1 + 2
else:
    total = None
    print(total)

############# while
a = 10
while 1 < a <= 10:
    print(f"Ana are{a} mere")

    if a % 2 == 0:
        continue
    a = a - 1

############ for
#lista = [41, 42, 43]
i = 'seara'
lista = "ana"
# for i in lista:
#     print(i)
#     print(i)
dictionar = {"a": 1, "b": 2}
for i in dictionar.keys():
    print(i)

##########
cuvant = "onomatopee"
cuvant_de_inlocuit = ""
for i in cuvant: "o"
if i != cuvant[0] and i != cuvant[-1]:
    cuvant_de_inlocuit = cuvant_de_inlocuit + "-"
else:
    cuvant_der_inlocuit = cuvant_de_inlocuit + 1
print(cuvant_de_inlocuit)
caracter_cerut = input("Alege o litera: ")
print(caracter_cerut)
while cuvant_der_inlocuit != cuvant:
    caracter_cerut = input("Alege o litera")
    print(caracter_cerut)
    if caracter_cerut in cuvant:
        # for i, v in enumarate(cuvant):
        #     lista_cuvant_der
            print(cuvant_de_inlocuit[i])

