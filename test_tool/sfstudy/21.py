


def isValid(s):
    if len(s) < 2:
        return False

    stack = ['1']
    dict = {'(':')','{':'}','[':']','1':'1'}

    for element in s:
        if element in dict:
            stack.append(element)
        elif dict[stack.pop()] != element:
            return False

    return len(stack) == 1

print(isValid('){'))

dict = {'(': ')', '{': '}', '[': ']'}



print(dict['('])
