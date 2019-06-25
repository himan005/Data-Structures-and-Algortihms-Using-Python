def in2infix(postfixExpression):
    stack = []

    for i in postfixExpression:
        if i.isalpha():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            c = b+i+a
            stack.append(c)
    return stack[-1]


postfix = input("Enter Expression")

infix = in2infix(postfix)

print(infix)