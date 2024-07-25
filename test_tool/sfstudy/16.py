


def isAnagram(s: str, t: str):
    if sorted(s) == sorted(t):
        return True
    else:
        return False






print(isAnagram('anagram','nagaram'))