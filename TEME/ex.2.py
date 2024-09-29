# 2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
#
# numar este par sau impar si afisati un raspuns in acest sens.


numar = int(input("Introduceti un numar: "))
rezultat = "par" if numar % 2 == 0 else "impar"
print(f"Numarul este {rezultat}.")
