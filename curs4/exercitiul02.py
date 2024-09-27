"""scrieti un program care itereaza prin primele 10 numere. La fiecare iteratie afiseaza suma dintre iteratorul curent
si urmatorul iterator din sir."""

'''
i = i
rezultatul = i + (i+1) = 1 + 2 +3
t = 2
rez = i+(i+2)= 2 + (2 + 1) = 5

i = 10
rez = 10 + (10-1) = 21
'''

rez = ()

for i in range(1, 11):
    rez = 2*i + 1

print(rez)