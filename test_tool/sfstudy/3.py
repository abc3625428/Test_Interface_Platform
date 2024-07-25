


def mgp(ls):
    mi = ls[0]
    res = 0
    for i in ls:
        res = max(res, i-mi)
        mi = min(mi, i)
    return res



ls = [1,2,3,4,5,6,3,2,4,3,4,3,5,575,875]

s = mgp(ls)
print(s)


