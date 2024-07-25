

def isHappy(n: int):

    ls = []

    while True:
        num = 0
        for i in str(n):
           num += int(i)**2
        if num == 1:
            return True
        else:
            if num in ls:
                return False
            ls.append(num)