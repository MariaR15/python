
# file = open('nume_fisier.txt')
# file = open('nume_fisier1.txt', 'a')
# file.write("hello\n")
# file.write("hello1\n")
# file.close()

# with open("nume_fisier1.txt", 'w') as file:
#     file.write("hello2")

# with open("nume_fisier.txt", "r") as file:
#     text = file.readlines()
#     print(text)
#     for line in text:
#         print(line)
# with open('nume_fisier.txt') as variabila:
#     a = list(variabila)
#     print(a)
#     for line in a:
#         print(line)

with open('nume_fisier.txt', 'r') as variabila:
    while True:
        line = variabila.readline()
        if not line:
            break
        print(line)