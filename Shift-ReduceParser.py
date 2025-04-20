grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "id"]
}

input_string = "id+id*id"
stack = "$"
input_string += "$"

def can_reduce(stack):
    for lhs, productions in grammar.items():
        for prod in productions:
            if stack.endswith(prod):
                return lhs, prod
    return None, None

print(f"{'Stack':<20}{'Input':<20}{'Action'}")
while True:
    print(f"{stack:<20}{input_string:<20}", end="")
    if input_string.startswith("id"):
        stack += "id"
        input_string = input_string[2:]
        print("Shift")
    elif input_string[0] in "+*()$":
        stack += input_string[0]
        input_string = input_string[1:]
        print("Shift")
    else:
        lhs, rhs = can_reduce(stack)
        if lhs:
            stack = stack[: -len(rhs)] + lhs
            print(f"Reduce by {lhs} -> {rhs}")
        elif stack == "$E$" and input_string == "":
            print("Accepted")
            break
        else:
            print("Reject")
            break
