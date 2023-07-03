def f1(s: str):
    i=int(s,base=16)
    return{
        "D1": i & 0b1111,
        "D2": (i >> 4) & 0b111111111,
        "D3": (i >> 13) & 0b11111111,
        "D4": (i >> 21) & 0b1111111111
    }

def f2(dct: dict):
    d1 = dct["D1"] << 18
    d2 = dct["D2"] << 22
    d3 = dct["D3"] << 10
    d4 = dct["D4"]
    return d1 | d2 | d3 | d4

def m(s: str):
    n = f1(s)
    return str(f2(n))

print(m('0x6354cc77'))