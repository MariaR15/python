# def functia_mea(param_1, param_2):
#     return "Ana are mere", "Ana are pere"
# rezultat = functia_mea(1, 2)
# print (rezultat)


def suma(a: int = 1, b: int = 2, c: int = 3, *args, **kwargs) -> (int, float):
    print(type(kwargs))
    suma = a + b + c
    for i in args:
        suma = suma + i
    for i in kwargs.values():
        suma = suma + i
    return suma, a- b
# rezultat = suma(1, 2)
# print(rezultat)
