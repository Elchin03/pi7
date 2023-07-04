import re

def m(s):
    r = r'"([^"]*)"\s*:\s*\[\s*([^]]*)'
    r1 = re.findall(r,s)
    ls={}
    for key, ints in r1:
        i1=ints.replace(" ","")
        i2 = i1.split(",")
        ls[key]=i2
    return ls
print(m('<block>{{ variable "ceordi_211": [ 7220 , -7601 , 3195]. }};{{variable"ququ":[ 9760 ,1816 , -9214]. }}; {{variable "ananat_401" : [1555 , -4200 ].}}; {{ variable"beanbi_162" : [ -5133 ,3994 , 2978 ,-6796 ]. }}; </block>'))

