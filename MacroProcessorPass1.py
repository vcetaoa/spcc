def macro_pass1(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    mnt = []
    mdt = []
    name_table = {}
    macro_name = ""
    arg_map = {}
    args = []
    in_macro = False

    for line in lines:
        words = line.strip().split()
        if not words:
            continue
        if words[0] == "MACRO":
            in_macro = True
            macro_name = words[1]
            args = [arg.replace("&", "") for arg in words[2:]]
            arg_map = {arg: f"#{i}" for i, arg in enumerate(args)}
            mnt.append(f"{macro_name} {' '.join(args)}")
            name_table[macro_name] = len(mdt)
        elif words[0] == "MEND":
            in_macro = False
            mdt.append("MEND")
        elif in_macro:
            for i in range(1, len(words)):
                if words[i].startswith("&"):
                    words[i] = arg_map[words[i].replace("&", "")]
            mdt.append(" ".join(words))

    with open("mnt.txt", "w") as mnt_file:
        for entry in mnt:
            mnt_file.write(entry + "\n")

    with open("mdt.txt", "w") as mdt_file:
        for entry in mdt:
            mdt_file.write(entry + "\n")

# Example usage:
macro_pass1("macro_input.txt")
