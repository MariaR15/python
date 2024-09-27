s = input("Introduceti un string: ")
n = input("Introduceti un numar:")

if n.isdigit():
    n = int(n)
    if n > len(s):
        pass
    else:
        s = s[n+1:]
    print(s)