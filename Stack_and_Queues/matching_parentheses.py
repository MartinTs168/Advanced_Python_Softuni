expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        opening_bracket_index = stack.pop()
        set_parentheses = expression[opening_bracket_index:i + 1]
        print(set_parentheses)