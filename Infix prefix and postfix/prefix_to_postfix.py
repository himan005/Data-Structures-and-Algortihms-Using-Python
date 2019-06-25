def in2postfix(prefixExpression):
    stack =[]
    postfix = ""

    for i in reversed(prefixExpression):

        if i.isalpha():
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            c = a+b+i
            stack.append(c)
    return stack[-1]


prefix = input("Enter Expression: ")

postfix = in2postfix(prefix)

print(postfix)
