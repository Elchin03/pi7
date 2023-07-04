import re


def m(s):
    r = r"list\(\s*([^)]*)\)-*>*\n*-*>*`([^ |]*)"
    r1 = re.findall(r, s)
    ls2 = []
    print(r1)
    for key, s1 in r1:
        ls = []
        k = key.replace(" ", "")
        for i in k.split(","):
            if i == ",":
                continue
            ls.append(i)
        p = (s1, ls)
        ls2.append(p)
    return ls2


print(
    m("<sect> || auto list( bibebi, anonxe_399 , beenla , inenma)->`sois_471 ||,||auto list( vegera_351 , inan_299 ,isqu, edis )->`tion_256||, || auto list(retiza_454 ,inen, atlaar , edri)->`raceace_7 ||, </sect>"))