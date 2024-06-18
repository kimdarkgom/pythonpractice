def m(v1,v2):
    rl = []
    r1 = v1+v2
    r2 = v1-v2

    rl.append(r1)
    rl.append(r2)

    return rl

ml = m(10, 20)
print(ml)