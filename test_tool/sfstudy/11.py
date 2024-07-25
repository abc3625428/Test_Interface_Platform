




def jsx(ransomNote,magazine):

    ra = sorted(ransomNote)
    ma = sorted(magazine)

    l = q = 0
    n = len(ra)-1
    m = len(ma)-1

    while l <= n and q <= m:
        if ra[l] == ma[q]:
            l += 1
            q += 1
        else:
            q += 1

    if  l > n:
        return True
    elif q > m:
        return False

print(jsx('bjaajgea',"affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"))
import collections
print(collections.Counter('affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec'))
print(collections.Counter('bjaajgea')-collections.Counter('affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec'))