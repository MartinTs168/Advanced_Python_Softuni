from custom_moduls.core import execute_expression


expression = input()

result = execute_expression(expression)
print(f"{result:.2f}")