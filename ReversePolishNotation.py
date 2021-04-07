# Reverse Polish Notation: It is a mathematical notation in which operators follow their operands. 
# For example, given `3 4 + 2 * 1 +`, the operation would be: (3+4) *2 +1 = 15.

def polish_eval(strArr):
    split_arr = strArr.split()
    stack = []

    for i in split_arr:
        if re.match ([\+\-\*\/], i):
            val2 = stack.pop()
            val1 = stack.pop()
						var = str(val1)+i+str(val2)
            stack.append(eval(var))
        else:
            stack.append(int(i))
    return stack[0]

print(polish_eval('3 4 + 2 * 1 +'))     # (3+4) *2 +1 = 15
print(polish_eval('3 5 + 7 2 – *'))     # (3+5)*(7–2) = 40