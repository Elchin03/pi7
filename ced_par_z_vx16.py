def m(s: str):
    i = int(s, base=16)
    h2 = ("H2", hex(i & 0b1))
    h3 = ("H3", hex((i >> 6) & 0b1111111))
    h4 = ("H4", hex((i >> 13) & 0b11111))
    sp = [h2, h3, h4]
    return sp


print(m('0x3c67d'))
