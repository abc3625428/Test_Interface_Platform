


def deaiwith(ls):

    mx = ls[0]
    for element in ls:
        if len(element) < len(mx):
            mx = element

    while mx != None:
        n = len(mx)

        s = 0
        ss = len(ls)
        for elements in ls:
            s += 1
            if mx not in elements[0:n]:
                mx = mx[:-1]
                break
            elif elements == ls[-1] and mx in elements and s == ss:
                return mx
    return ""


res = deaiwith(["flower","flawer","flvwer","flower"])
print(res)
