def f1(s: str):
    i=int(s)
    return{
        "Z1": i & 0b111,
        "Z2": (i >> 3) & 0b1111,
        "Z3": (i >> 7) & 0b111111,
        "Z4": (i >> 13) & 0b111111,
    }
def f2(dct: dict):
    z1 = dct["Z1"]
    z2 = dct["Z2"] << 3
    z3 = dct["Z3"] << 14
    z4 = dct["Z2"] << 7
    return  z1 | z2 | z3 | z4

def m(n: str):
    dct = f1(n)
    return str(f2(dct))

print(m('215564')) #Реализовать функцию для транскодирования данных, содержащих битовые поля. Входные данные: Десятичная строка. Выходные данные: Целое.

