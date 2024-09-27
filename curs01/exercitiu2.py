
numar_telefoane = input("Introdu numarul de telefon: ")
if len(numar_telefoane)== 12:
    if numar_telefoane[0: 3] =='+40':
        if numar_telefoane[3: 13].isdigit():
            print('numar')