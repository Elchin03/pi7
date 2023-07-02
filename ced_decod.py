def decod(dct):
    h1 = int(dct["H1"], base=16)
    h2 = int(dct["H2"], base=16) << 10
    h3 = int(dct["H3"], base=16) << 20
    h4 = int(dct["H4"], base=16) << 33
    h5 = int(dct["H5"], base=16) << 40

    return str(h1 | h2 | h3 | h4 | h5)


print(decod('0x1a4fb7a50867'))
