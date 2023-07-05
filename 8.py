import re


def main(s):
    r = r'auto\s*([^ ]*)\s*::=\s*\[\s*q\(([^]]*)'
    r1 = re.findall(r, s)
    p = {}
    for key, s1 in r1:
        ls = []
        r3 = s1.replace("q(", "")
        r4 = r3.replace(")", "")
        r5 = r4.replace(".", "")
        r6 = r5.split()
        p[key] = r6
    return p
