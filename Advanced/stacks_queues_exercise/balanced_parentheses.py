opening_brackets = ["[", "{", "("]
closing_brackets = ["]", "}", ")"]


def check_parentheses(sequence):
    stack = []
    for element in sequence:
        if element in opening_brackets:
            stack.append(element)
        elif element in closing_brackets:
            index = closing_brackets.index(element)
            if len(stack) > 0 and opening_brackets[index] == stack[-1]:
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


text = input()
print(check_parentheses(text))