


def pdzc(s,t):

    for element in t:
        if s == '':
            break

        if element == s[0]:
            s = s[1:len(s)]

    if s == '':
        return True
    else:
        return None









res = pdzc('b','abc')
print(res)


