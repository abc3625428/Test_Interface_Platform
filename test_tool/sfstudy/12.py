

def tgzf(s,t):

    if len(s) != len(t):
        return False

    import collections

    s = collections.Counter(s)
    t = collections.Counter(t)

    ss=[]
    tt=[]
    for key,value in s.items():
        ss.append(value)
    for key,value in t.items():
        tt.append(value)


    print(ss,tt)
    if sorted(ss) == sorted(tt):
        return True
    else:
        return False

def tgzfz(s,t):


    mp1 , mp2 = {} ,{}
    for a,b in zip(s,t):
        print(a,b)
        print(mp2,mp1)

        if a in mp1 and mp1[a] != b:
            return False

        if b in mp2 and mp2[b] != a:
            return False

        mp1[a] = b
        mp2[b] = a



print(tgzfz('paper','title'))

s = {'a':'b'}
print('a' in s,'b' in  s)