import re

def m(s):
    r = r"q\(([^)]*\))\s*:\s*#([^ ]*)"
    z= re.findall(r,s)
    l2=[]
    # for s1, ints in z:
    #     l=(s1,ints)
    #     l2.append(l)
    # return l2
    return z
print(m("<block> begin local q(zaxedi_23) : #8577 end; begin local q(lemaan_61) : #8852 end; begin local q(inri): #-6505 end;</block>"))

