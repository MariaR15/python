# 3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
#
# bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
#
# la 4 (fara rest)

an = int(input("Introduceti un an: "))

# vad daca anul e bisect
if an % 4 == 0:
    print("Anul este bisect.")
else:
    print("Anul nu este bisect.")
# so, daca impartind la 4 o sa am 1 nu e bisect
# 2025 % 4 = 1 (deci 2021 nu este bisect)
# 2024 % 4 = 0 (deci 2020 este bisect)