import re


def mumu(x):
    r = r"array\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    z = re.findall(r, x)
    ls2 = []
    for ints, key in z:
        ls = []

        for i in ints.split():
            if i == ".":
                continue
            ls.append(i)
        p = (key, ls)
        ls2.append(p)
        print(ints, key)
    return ls2


print(mumu(
    ".do | glob array( tear . usraza_742 . aes_561 ) => aqulete_707.|;|glob array( ussote_180 . arbila ) => ordi_963. |; |glob array(arsoare . ate ) => isrete. |; .end))"))
