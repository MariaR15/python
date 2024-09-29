# 1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
#
# caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
#
# In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
#
# caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
#
# preluat automat de la tastatura.


nume = input("introduceti numele : ")
text = input("introduceti un text: ")

# isalpha --> verific daca sirul de caractere are doar litere
if text.isalpha():
    print("sirul de caractere a fost gasit de " + nume)
# isdigit --> folosesc pentru cifre
elif text.isdigit():
    print("Sirul dat este un sir de numere.")
else:
    print("Sirul dat contine caractere mixte.")
