# method that returns priority of operator


def priority(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


# method to convert infix expression into postfix expression assuming all expressions are valid
def in2postfix(infixExpression):

    stack = []

    postfixExpression = ""

    i = 0

    while i in range(0, len(infixExpression)):

        # if an alphabet is found in expression then copy it to postfixExpression
        if infixExpression[i].isalpha():
            postfixExpression += infixExpression[i]

        # if an opening bracket is found in expression then put them in stack
        elif infixExpression[i] == '(' or infixExpression[i] == '[' or infixExpression[i] == '{':
            stack.append(infixExpression[i])

        # if an closing bracket is found in infixExpression keep removing operators from stack and
        # add them to postfix expression
        elif infixExpression[i] == ')' or infixExpression[i] == ']' or infixExpression[i] == '}':

            if infixExpression[i] == ')':
                while stack[-1] != '(':
                    postfixExpression += stack.pop()
                stack.pop()

            if infixExpression[i] == ']':
                while stack[-1] != '[':
                    postfixExpression += stack.pop()
                stack.pop()

            if infixExpression[i] == '}':
                while stack[-1] != '{':
                    postfixExpression += stack.pop()
                stack.pop()

        # if none of above case are satisfy then we surely have an operator
        else:

            # if stack is empty then we simply put operator in stack
            if len(stack) == 0:
                stack.append(infixExpression[i])

            # if not then we compare priority of stack top and current operator
            else:

                # if priority of current operator if high then push it onto stack
                if priority(infixExpression[i]) > priority(stack[-1]):
                    stack.extend(infixExpression[i])

                # if priority if current operator is less than or equal to stack top then
                # pop stack top and add it to postfixExpression
                elif priority(infixExpression[i]) <= priority(stack[-1]):
                    postfixExpression += stack.pop()
                    position = len(stack) - 1

                    # if an operator that has equal priority as of current operator then pop
                    while position >= 0 and priority(stack[position]) == priority(infixExpression[i]):
                        postfixExpression += stack.pop()
                        position -= 1
                        if position < 0:
                            break

                    stack.extend(infixExpression[i])

        i += 1

    while len(stack) != 0:
        postfixExpression += stack.pop()

    return postfixExpression


infix = input("Enter infix Expression:")

postfix = in2postfix(infix)

print(postfix)