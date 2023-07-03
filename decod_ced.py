def de(s: str):
    i = int(s)
    return {
        "X1": str(i & 0b11111111),
        "X2": str((i >> 8) & 0b111),
        "X3": str((i >> 11) & 0b111111111),
    }


print(de('525378'))
