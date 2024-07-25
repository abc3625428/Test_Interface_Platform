
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        ls = []
        while head.next == True:
            if head.next not in ls:
                ls.append(head.next)
            else:
                return False
        return True
