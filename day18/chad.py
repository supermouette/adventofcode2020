def is_int(x):
    try:
        int(x)
        return True
    except:
        return False


def find_exprr(string):
    print("---", string)
    count_p = 0
    sub_exprr = False
    for i in range(len(string)):
        if string[i] == '(':
            count_p += 1
            sub_exprr = True
        elif string[i] == ")":
            count_p -= 1
        elif (string[i] == " " and count_p == 0) or len(string) - 1 == i:
            if sub_exprr:
                value = solve(string[1:i - 1])
            else:
                value = int(string[:i + int(len(string) - 1 == i)])
            i1 = i
            break
    return value, i1, sub_exprr


def solve(string):
    print(string)
    new_string = string[:]
    while not is_int(new_string):
        value_1, i1, _ = find_exprr(new_string)
        value_2, i2, _ = find_exprr(new_string[i1+3:])
        op = new_string[i1+1]
        value = value_1*value_2 if op == "*" else value_1+value_2
        new_string = str(value) + new_string[i1+3+i2:]
        print(new_string, "---", value_1, value_2, value, i2)
    return int(new_string)


with open("input.txt", "r") as f:
    lines = [line.strip("\n") for line in f.readlines()]

print(solve(lines[0]))
