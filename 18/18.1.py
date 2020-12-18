from collections import deque

operators = {"+": lambda x,y: x+y, "*": lambda x,y:x*y, }

def sum_expressions(input):
    sum = 0
    for line in input:
        stack = deque()
        for char in line:
            if char == " ":
                continue
            elif char in operators:
                stack.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                char = stack.pop()
                stack.pop()
                stack.append(char)
            else:
                char = int(char)
                stack.append(char)
            while len(stack) >= 3 and stack[-2] in operators and stack[-1] != "(":
                operand1 = stack.pop()
                operator = stack.pop()
                operand2 = stack.pop()
                char = operators[operator](operand1, operand2)
                stack.append(char)
        sum += stack[0]
    return sum
input = open('18/input.txt').read().splitlines()
print(sum_expressions(input))