def precedence(op):
    return 2 if op in ("*", "/") else 1

def infix_to_postfix(expr):
    stack = []
    output = []
    for ch in expr:
        if ch.isalnum():
            output.append(ch)
        elif ch in "+-*/":
            while stack and precedence(stack[-1]) >= precedence(ch):
                output.append(stack.pop())
            stack.append(ch)
    while stack:
        output.append(stack.pop())
    return output

def generate_3ac(postfix):
    stack = []
    temp_counter = 1
    tac = []
    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            temp = f"t{temp_counter}"
            tac.append(f"{temp} = {a} {token} {b}")
            stack.append(temp)
            temp_counter += 1
    return tac

# Example:
expr = "a+b*c"
postfix = infix_to_postfix(expr)
tac = generate_3ac(postfix)
for line in tac:
    print(line)
