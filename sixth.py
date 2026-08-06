def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0

def infix_to_postfix(exp):
    stack = []
    postfix = ""

    for ch in exp:
        if ch.isalnum():        
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:                     
            while stack and precedence(ch) <= precedence(stack[-1]):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

exp = input("Enter Infix Expression: ")
result = infix_to_postfix(exp)
print("Postfix Expression:", result)

