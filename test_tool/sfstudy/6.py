

def split_list(str):

    ls = []
    for element in str[::-1]:
        if element == " " and len(ls)>0:
            return len(ls)
        elif element != ' ':
            ls.append(element)
    return len(ls)



res  = split_list("   fly me   to   the moon  ")
print(res)