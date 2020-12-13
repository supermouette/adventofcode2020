def bezout(a, b):
    (u0, v0, u1, v1)=(1, 0, 0, 1)
    while b:
        (q, r) = divmod(a, b)
        (a, b) = (b, r)
        (u0, v0, u1, v1) = (u1, v1, u0-q*u1, v0-q*v1)
    return u0, v0


with open("input.txt", "r") as f:
    lines = f.readlines()

buses = []
splited = lines[1].strip("\n").split(",")
for i in range(len(splited)):
    if splited[i] != "x":
        buses.append([int(splited[i]), (int(splited[i]) - i) % int(splited[i])])

# As bus ID are all prime number, it works
print(buses)
u, v = bezout(buses[0][0], buses[1][0])
x0 = buses[0][0]*buses[1][1]*u + buses[1][0]*buses[0][1]*v
new_n = buses[0][0]*buses[1][0]
x0 = x0 % new_n

for i in range(2, len(buses)):
    u, v = bezout(new_n, buses[i][0])
    x0 = new_n * buses[i][1]*u + buses[i][0]*x0*v
    new_n *= buses[i][0]
    x0 = x0 % new_n

print(x0)
