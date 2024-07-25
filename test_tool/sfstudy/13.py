

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(" ")):
            return False

        mp1 , mp2 = {} ,{}
        for a,b in zip(pattern,s.split(" ")):

            if a in mp1 and mp1[a] != b:
                return False
            if b in mp2 and mp2[b] != a:
                return False
            mp1[a] = b
            mp2[b] = a


        return True