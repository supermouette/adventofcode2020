import matplotlib.pyplot as plt
from math import cos, sin, pi

with open("input.txt", "r") as file:
    moves = [[line[0], int(line[1:-1])] for line in file.readlines()]


orientation = {0: "E", 90: "N", 180: "W", 270: "S", 360: "E"}
instruction = {"N": lambda arg, p, f: ([p[0]+arg, p[1]], f),
               "S": lambda arg, p, f: ([p[0]-arg, p[1]], f),
               "E": lambda arg, p, f: ([p[0], p[1]+arg], f),
               "W": lambda arg, p, f: ([p[0], p[1]-arg], f),
               "L": lambda arg, p, f: (p, (f+arg) % 360),
               "R": lambda arg, p, f: (p, (f-arg) % 360),
               "F": lambda arg, p, f: instruction[orientation[facing]](arg, p, f)}

pos = [0, 0]
facing = 0
plt.scatter([pos[0]], [pos[1]], s=64, c="r")
history = [[pos[0]], [pos[1]]]
for move in moves:
    pos, facing = instruction[move[0]](move[1], pos, facing)
    history[0].append(pos[0])
    history[1].append(pos[1])
print(pos, sum(pos))
plt.plot(history[0], history[1])
plt.scatter([pos[0]], [pos[1]], s=64, c="g")
plt.show()
