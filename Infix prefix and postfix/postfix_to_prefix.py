def in2prefix(postfixExpression):

    stack = []
    for i in postfixExpression:
        if i.isalpha():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            c = i+b+a
            stack.append(c)
    return stack[-1]


postfix = input("Enter Expression")

prefix = in2prefix(postfix)

print(prefix)