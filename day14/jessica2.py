with open("input.txt", "r") as f:
    lines = [line.strip('\n').split(" = ") for line in f.readlines()]
mem = {}
mask1 = 0
max_int = int("1"*36, 2)
for instruction in lines:
    if instruction[0] == "mask":
        mask = instruction[1]
        maskX = mask[::-1]
        mask1 = int(mask.replace("X", "0"), 2)
    else:
        address = int(instruction[0][4:-1])
        value = int(instruction[1])
        address |= mask1
        x_i = [i for i, c in enumerate(maskX) if c == "X"]
        x_list = []
        for i in range(2**len(x_i)):
            x_list.append({})
            b = format(i, '#0' + str(2+len(x_i)) + 'b')[2:]
            for j in range(len(x_i)):
                x_list[-1][x_i[j]] = b[j]
        for i in x_list:
            new_address = address
            for j in i:
                if i[j] == '1':
                    new_address = new_address | (1 << j)
                else:
                    new_address = new_address & ~(1 << j)
            mem[new_address] = value

print(sum(mem.values()))
# not 185698701239