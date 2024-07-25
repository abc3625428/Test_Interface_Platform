
import random

def efcz(ls,t):
    r = len(ls)-1
    l = 0
    while l <= r:
        mid = (l+r)//2

        if ls[mid] > t:
            r = mid -1
        elif ls[mid] < t:
            l = mid +1
        else:
            return mid

    return -1

print(efcz([1,3,4,5,7,8,9,12,14,15,16,19,33],3))


p = list(range(100))
random.shuffle(p)

print(p)


def mppx(ls):
    for i in range(len(ls)-1):
        for j in range(len(ls)-1):
            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]
    return ls

# print(mppx(p))


def jbpx(ls,l,r):
    mid = ls[l]
    while l<r:
        while l<r and mid <= ls[r]:
            r-=1
        ls[l] = ls[r]
        while l<r and  mid >= ls[l]:
            l+=1
        ls[r] = ls[l]
    ls[r] = mid
    return r

def ks_sort(ls,l,r):
    if l<r:
        mid = jbpx(ls,l,r)
        ks_sort(ls,l,mid-1)
        ks_sort(ls,mid+1,r)
    return ls

# print(ks_sort(p,0,len(p)-1))


def merge(ls,l,mid,r):
    i = l
    j = mid+1
    itme = []

    while i<=mid and j<=r:
        if ls[i] < ls[j]:
            itme.append(ls[i])
            i+=1
        else:
            itme.append(ls[j])
            j+=1

    while i<=mid:
        itme.append(ls[i])
        i+=1

    while j<=r:
        itme.append(ls[j])
        j+=1

    ls[l:r+1] = itme
    print(itme)

def gb_sort(ls,l,r):

    if l<r:
        mid = (l+r)//2
        gb_sort(ls, l, mid)
        gb_sort(ls, mid+1, r)
        merge(ls,l,mid,r)

    return ls

# print(gb_sort(p,0,len(p)-1))

def time_num(func):
    def zxcv(*args, **kwargs):
        import datetime
        st = datetime.datetime.now()
        result = func(*args, **kwargs)
        et = datetime.datetime.now()
        print(et-st)
        return result
    return zxcv

@time_num
def ls_qc(ls):

    li = []
    for i in ls:
        if i not in li:
            li.append(i)

    print(list(range(1000000)))
    return li

ls = [1,2,2,2,12,12,1,23,2,4,24,23,3,32,4,234,123,12,3,12,31,23,12,31,23,12,123,3]
mppx(ls)
print(ls_qc(ls))



class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

def carete_node(item):
    head = Node(item[0])
    for element in item[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

carete_node(item=[1,2,3,4,5,7,8])



