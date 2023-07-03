def dec(s: str):
    i = int(s)
    return {
        "M1": hex(i & 0b1111),
        "M3": hex((i >> 6) & 0b1111111111),
        "M4": hex((i >> 16) & 0b11111111),
        "M5": hex((i >> 24) & 0b111111),
    }


print((dec('538511042')))
