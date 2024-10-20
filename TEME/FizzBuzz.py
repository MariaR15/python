
numar = int(input("Introduc un nr intreg: "))

if numar % 3 == 0 and numar % 5 == 0:
    print("FizzBuzz")
elif numar % 3 == 0:
    print("Fizz")
elif numar % 5 == 0:
    print("Buzz")
else:
    print(numar)
