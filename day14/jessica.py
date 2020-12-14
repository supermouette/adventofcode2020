with open("input.txt", "r") as f:
    lines = [line.strip('\n').split(" = ") for line in f.readlines()]
mem = {}
mask1 = 0
mask0 = 0
max_int = int("1"*36, 2)
for instruction in lines:
    if instruction[0] == "mask":
        mask = instruction[1]
        mask1 = int(mask.replace("X", "0"), 2)
        mask0 = int(mask.replace("1", "X").replace("0", "1").replace("X", "0"), 2)
    else:
        address = int(instruction[0][4:-1])
        value = int(instruction[1])
        value |= mask1
        value &= ~mask0 & max_int
        mem[address] = value

print(sum(mem.values()))
