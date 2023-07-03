import re

def mu(x):
    r = r"\[\[\s*variable\s*list\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    z = re.findall(r, x)
    ls2 = []
    print(z)
    print()
    for ints, key in z:
        ls = []
        print(ints)
        for i in ints.split():
            if i == ".":
                continue
            ls.append(int(i))
        p = (key, ls)
        ls2.append(p)
    return ls2

print(mu("begin [[ variable list(-8983 . 6385 )=>aoren_461. ]], [[variablelist( -6192 . 4321 . -1780 . 955) =>riuser_156. ]],[[ variablelist(-9612 . -2556) =>eres.]], [[ variable list( -9853 . -4639 . -2997) => zaisa_42. ]], \end"))