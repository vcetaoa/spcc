def constant_folding(code):
    optimized = []
    for line in code:
        if "=" in line:
            var, expr = line.split("=")
            try:
                result = eval(expr)
                optimized.append(f"{var.strip()} = {result}")
            except:
                optimized.append(line)
        else:
            optimized.append(line)
    return optimized

def constant_propagation(code):
    constants = {}
    optimized = []
    for line in code:
        if "=" in line:
            var, expr = line.split("=")
            if expr.strip().isdigit():
                constants[var.strip()] = expr.strip()
            for k, v in constants.items():
                expr = expr.replace(k, v)
            optimized.append(f"{var.strip()} = {expr}")
        else:
            optimized.append(line)
    return optimized

def dead_code_elimination(code):
    used_vars = set()
    for line in reversed(code):
        tokens = line.replace("=", " ").split()
        used_vars.update(tokens[1:])
    return [line for line in code if line.split("=")[0].strip() in used_vars]

def common_subexpression_elimination(code):
    expr_table = {}
    optimized = []
    for line in code:
        if "=" in line:
            var, expr = line.split("=")
            if expr in expr_table:
                optimized.append(f"{var.strip()} = {expr_table[expr]}")
            else:
                expr_table[expr] = var.strip()
                optimized.append(line)
        else:
            optimized.append(line)
    return optimized

def loop_unrolling(loop_code, times):
    return [line for line in loop_code for _ in range(times)]

# Example:
if __name__ == "__main__":
    code = ["a = 2 + 3", "b = a", "c = b + 5"]
    print("Constant Folding:", constant_folding(code))
    print("Propagation:", constant_propagation(code))
    print("Dead Code:", dead_code_elimination(code))
    print("Common Subexpr:", common_subexpression_elimination(code))
    print("Loop Unrolling:", loop_unrolling(["x = x + 1"], 3))
