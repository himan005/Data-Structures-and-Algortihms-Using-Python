def reverse(prefixExpression):
    return "".join(reversed(prefixExpression))


def in2infix(prefixExpression):

    prefixExpression = reverse(prefixExpression)
    stack = []
    infix = ""
    i = 0
    while i in range(0, len(prefixExpression)):
        if prefixExpression[i].isalpha():
            stack.extend(prefixExpression[i])
        else:
            a = stack.pop()
            b = stack.pop()
            c = a+prefixExpression[i]+b
            stack.append(c)
        i+=1
    while len(stack)!= 0:
        infix += stack.pop()
    return infix


prefix = input("Enter infix Expression")

infix = in2infix(prefix)

print(infix)

