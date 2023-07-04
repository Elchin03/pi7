import re

def m(s):
    r = r'"([^"]*)"\s*=\s*#([^ \n]*)'
    r1 = re.findall(r,s)
    l={}
    for key,ints in r1:
        l[key]=ints
    return l

print(m('<section> .do decl @"arvege" =#4824 .end. .do decl @"aran_761"=#955 .end. .do decl @"onsoxe"= #-8772 .end.</section>'))
