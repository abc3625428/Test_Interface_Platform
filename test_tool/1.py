def remove_nested_brackets(input_string):
    stack = []
    output_parts = []

    for char in input_string:

        if char == '(':

            if stack.count('(') > 0:
                stack.append(char)
            else:
                stack.append(char)
                output_parts.append(char)

        elif char == ')':
            if stack:
                stack.pop()
                if stack.count('(') == 1:
                    output_parts.append(char)
                    stack.pop()
            else:
                pass
        else:
            output_parts.append(char)


    return ''.join(output_parts)

input_string = "(1,(2,((3,4)),5,((6,7),8"
print(remove_nested_brackets(input_string))
