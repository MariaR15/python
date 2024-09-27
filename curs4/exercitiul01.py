# Se cer 2 nr intregi de la tastatura. Sa se calculeze produsul daca produsul dintre cele 2 numere este
# mai mic sau egal cu 1000, altfel, sa se returneze suma acestora."""
text1 = input("Introduceti nr1")
text2 = input("Introduceti nr2")
produs = None
suma = None

rezultat = None
operatie = None

if text1.isdigit() and text2.isdigit():
    text1 = int(text1)
    text2 = int(text2)
    produs = text1 * text2
    if (rezultatul := text1 * text2) and rezultatul <= 1000:
        operatie = "produs"

    else:
        rezultat = text1 + text2
        operatie = "suma"

    if operatie == "produs":
        print(f"{operatie} este{rezultat} ")
