


def lmsz(s):

    di = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }

    res = 0
    n = len(s)
    for i,j in enumerate(s):
        value = di[j]
        if i < n-1 and value < di[s[i+1]]:
            res -= value
        else:
            res += value

    return res





s = lmsz('MCMXCIV')
print(s)