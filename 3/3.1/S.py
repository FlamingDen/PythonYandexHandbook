inp = list(input().split())
stack = []

for curr in inp:
    if curr.isdigit():
        stack.append(int(curr))
    else:
        b = stack.pop()
        a = stack.pop()
        if curr == "+":
            stack.append(a + b)
        elif curr == "-":
            stack.append(a - b)
        else:
            stack.append(a * b)

print(stack[0])
