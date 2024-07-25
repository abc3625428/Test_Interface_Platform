



def dealtwith(s):
    if len(s) < 2:
        return True

    while s.isalnum() == False:

        for i in s:
            if i.isdigit() or i.isalpha():
                continue
            else:
                s = s.replace(i, '')

    c = s.lower()

    if c == c[::-1]:
        return True
    else:
        return False





s = ",."
print(dealtwith(s))
