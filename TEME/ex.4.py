# 4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
#
# este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
#
# decat 10 si afisati un mesaj de confirmare..Daca numarul este zero afisati “Numarul
#
# este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
#
# afisati numarul pozitiv.
#
# fc care arata ce nr am adaugat
def verifica_numar(numar):
    if numar > 0:
        if numar < 10:
            return "Nr e pozitiv si mai mic decat 10."
        else:
            return "Nr este + si mai mare sau egal cu 10."
    elif numar == 0:
        return "Nr este 0."
    # dc nr e -
    else:
        numar_positiv = -numar  # fac nr sa fie +
        return f"Nr negativ a fost facut in pozitiv: {numar_positiv}."

input_numar = input("Introduceti un nr: ")

try:
    numar = float(input_numar)
    rezultat = verifica_numar(numar)
    print(rezultat)
except ValueError:
    print("Te rog, introdu un numar valid!")  
