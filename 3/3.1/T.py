inp = list(input().split())
stack = []

for curr in inp:
    if curr.isdigit():
        stack.append(int(curr))
    else:
        
        if curr == "+":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif curr == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif curr == "*":
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif curr == "/":
            b = stack.pop()
            a = stack.pop()
            stack.append(a // b)
        elif curr == "~":
            a = stack.pop()
            stack.append(-a)
        elif curr == "!":
            b = stack.pop()
            res = 1
            for i in range(1, b + 1):
                res *= i
            stack.append(res)
        elif curr == "#":
            stack.append(stack[len(stack) - 1])
        elif curr == "@":
            b = stack.pop()
            a = stack.pop()
            c = stack.pop()
            stack.append(a)
            stack.append(b)
            stack.append(c)

print(int(stack[0]))
