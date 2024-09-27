"""scrieti un program care sa extraga inversul dintr-un nr.
Exemplu: 7536 trebuie afisati 6 3 5 7"""

text = input("Introdu numar dorit:")
# print(text[::-1])
new_text = ""

for i in text:
    new_text = i + new_text
print(new_text)
