tree = ({"ABAP", 1978, "ROFF", 1970},
        {"ABAP", 1978, "ROFF", 1990},
        {"ABAP", 1978, "ROFF", 1969},
        {"ABAP", 1978, "LESS"},
        {"ABAP", 1978, "GAMS", "SELF"},
        {"ABAP", 1978, "GAMS", "TXL"},
        {"ABAP", 1978, "GAMS", "SCAML"},
        {"ABAP", 1988},
        {"RUBY", 1970, "SELF", 1978},
        {"RUBY", 1970, "SELF", 1998},
        {"RUBY", 1970, "TXL"},
        {"RUBY", 1970, "SCAML"},
        {"RUBY", 1990},
        {"RUBY", 1969})


def s(r):
    s1 = set(r)
    return [i for i in range(len(tree))
            if not (len(tree[i]-s1))][0]
print(s([1978, 'RUBY', 'SELF', 1970, 'ROFF']))