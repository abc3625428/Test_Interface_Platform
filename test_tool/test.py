

class Listnode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class singlinklist():
    def create(self,list):
        lenth = len(list)
        if lenth == 0:
            return None
        head = Listnode(list[0],None)
        tail = head
        for i in range(lenth-1):
            node = Listnode(list[i+1],None)
            tail.next = node
            tail = node

        return head

    def scan(self,linklist):
        tail = linklist
        list =[]
        while tail:
            list.append(tail.val)
            tail = tail.next
        return list


lb = singlinklist()

l1 = [1,3,5,6,7,8,9,43,54,63,73,85]
l2 = [1,2,3,23,24,25,26,27,28,30,33,35,36,61]
c = singlinklist()
ls1 = c.create(list=l1)
ls2 = c.create(l2)




class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        elif l1 and not l2:
            return l1
        tail1=l1
        tail2=l2
        if tail1.val<tail2.val:
            head=tail1
            tail1=tail1.next
            head.next=None
        else:
            head=tail2
            tail2=tail2.next
            head.next=None
        tail=head
        while(tail1 and tail2):
            if tail1.val<tail2.val:
                tail.next=tail1
                tail1=tail1.next
                tail=tail.next
                tail.next=None
            else:
                tail.next=tail2
                tail2=tail2.next
                tail=tail.next
                tail.next=None
        if tail1:
            tail.next=tail1
        elif tail2:
            tail.next=tail2
        return head


s = Solution()
res = s.mergeTwoLists(ls1,ls2)

import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))

print(list(range(30)))


