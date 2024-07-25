


def kssf(haystack,needle):

    h = len(haystack)
    n = len(needle)
    m = 0
    while n<=h:
        if needle not in haystack[m:n]:
            m += 1
            n += 1
        else:
            return m
    return -1


res = kssf("sadbutsad","sad")
print(res)