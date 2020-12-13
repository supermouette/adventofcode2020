with open("input.txt", "r") as f:
    lines = f.readlines()

buses = []
splited = lines[1].strip("\n").split(",")
for i in range(len(splited)):
    if splited[i] != "x":
        buses.append([int(splited[i]), (int(splited[i]) - i) % int(splited[i])])

# As bus ID are all prime number, I could use bezout identity to solve, but I don't want to.

buses.sort(key=lambda e: -e[0])
print(buses)
i = buses[0][1]
while True:
    i += buses[0][0]
    for j in range(1, len(buses)):
        if i % buses[j][0] != buses[j][1] % buses[j][0]:
            break
    else:
        print(i)
        break
