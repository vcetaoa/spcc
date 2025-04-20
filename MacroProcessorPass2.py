MNT = {"INCR": 0}
MDT = ["LDA #0", "ADD #1", "STA #0", "MEND"]
ALA = []

def macro_pass2(source_code):
    expanded_code = []
    for line in source_code:
        words = line.strip().split()
        if not words:
            continue
        if words[0] in MNT:
            mdt_index = MNT[words[0]]
            args = words[1:]
            ALA.clear()
            for i, arg in enumerate(args):
                ALA.append(arg)

            i = mdt_index
            while MDT[i] != "MEND":
                mdt_line = MDT[i]
                for j, arg in enumerate(ALA):
                    mdt_line = mdt_line.replace(f"#{j}", arg)
                expanded_code.append(mdt_line)
                i += 1
        else:
            expanded_code.append(line)
    
    return expanded_code

# Example usage:
source_program = [
    "INCR A B",
    "MOV A B"
]
expanded = macro_pass2(source_program)
for line in expanded:
    print(line)
