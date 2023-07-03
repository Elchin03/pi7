import re

def m(s):
    r = r"('[^']*)'\s*->\s*([^.]*)"
    r1= re.findall(r,s)
    l2=[]
    for key,s1 in r1:
        l=(s1,key)
        l2.append(l)
    return l2

print(m("<%(( store'onaror' -> sodiis. )). ((store 'tiatso_840'-> riqu. )). (( store 'esri_682' -> geante_115. )). ((store 'aror'-> anquve_641. )). %>"))