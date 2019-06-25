# method to reverse infix Expression
def reverse(infixExpression):
    return "".join(reversed(infixExpression))


# method that return priority of operator
def priority(operator):
    if operator == '+' or operator == '-':
        return 1

    elif operator == '*' or operator == '/' or operator == '%':
        return 2

    elif operator == '^':
        return 3

    else:
        return 0


# function to convert infixExpression to prefixExpression
def in2prefix(infixExpression):

    infixExpression = reverse(infixExpression)

    stack = []

    prefixExpression = ""

    i = 0

    while i in range(0, len(infixExpression)):

        # if a alphabet is found then copy it to input Expression
        if infixExpression[i].isalpha():
            prefixExpression += infixExpression[i]

        # as we reverse expression first closing brackets found first
        # and put it in stack
        elif infixExpression[i] == ')' or infixExpression[i] == ']' or infixExpression[i] == '}':
            stack.append(infixExpression[i])

        # if a opening bracket if found then
        # keep removing operators from stack and add them in prefixExpression until
        # ou find corresponding opening bracket

        elif infixExpression[i] == '(' or infixExpression[i] == '[' or infixExpression[i] == '{':

            if infixExpression[i] == '(':
                while stack[-1] != ')':
                    prefixExpression += stack.pop()
                stack.pop()

            if infixExpression[i] == '[':
                while stack[-1] != ']':
                    prefixExpression += stack.pop()
                stack.pop()

            if infixExpression[i] == '{':
                while stack[-1] != '}':
                    prefixExpression += stack.pop()
                stack.pop()

        # if none of above cases are satisfied then we surly have an operator
        else:

            # if stack is empty then we simply put operator in stack
            if len(stack) == 0:
                stack.append(infixExpression[i])

            # if stack is not empty we compare priority of top stack and current operator
            else:

                # if priority of current operator is greater than or equal to stack top then push it
                # onto stack
                if priority(infixExpression[i]) >= priority(stack[-1]):
                    stack.extend(infixExpression[i])

                # if the priority of current operator is less than stack top then
                # pop stack top and add to prefixExpression
                elif priority(infixExpression[i]) < priority(stack[-1]):
                    prefixExpression += stack.pop()
                    position = len(stack) - 1

                    # now if you have an operator that has less priority as of current operator then pop
                    while position >= 0 and priority(stack[position]) > priority(infixExpression[i]):
                        prefixExpression += stack.pop()
                        position -= 1
                        if position < 0:
                            break
                    stack.extend(infixExpression[i])

        i += 1

    while len(stack) != 0:
        prefixExpression += stack.pop()

    prefixExpression = reverse(prefixExpression)

    return prefixExpression

infix = input("Enter Expression:")

prefix = in2prefix(infix)

print(prefix)











