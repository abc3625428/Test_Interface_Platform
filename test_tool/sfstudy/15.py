


def tgzfz(pattern, s):


    mp1 , mp2 = {} ,{}
    for a,b in zip(pattern,s.split(" ")):

        print(mp2,mp1)
        if a in mp1 and mp1[a] != b:

            return False
        if b in mp2 and mp2[b] != a:
            return False

        mp1[a] = b
        mp2[b] = a

    return True



print(tgzfz('abba','dog cat cat dog'))


pattern = 'aaa'
s = "aa aa aa aa"
ss = ''.join(pattern)
print(ss)
print()

