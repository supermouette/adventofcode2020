import matplotlib.pyplot as plt
from math import cos, sin, pi

with open("input.txt", "r") as file:
    moves = [[line[0], int(line[1:-1])] for line in file.readlines()]


def rotate(p, angle):
    theta = angle*pi/180
    cos_a = cos(theta)
    sin_a = sin(theta)
    x = cos_a * p[0] - sin_a * p[1]
    y = sin_a * p[0] + cos_a * p[1]
    return [round(x), round(y)]


instruction = {"E": lambda arg, p, w: (p, [w[0]+arg, w[1]]),
               "W": lambda arg, p, w: (p, [w[0]-arg, w[1]]),
               "N": lambda arg, p, w: (p, [w[0], w[1]+arg]),
               "S": lambda arg, p, w: (p, [w[0], w[1]-arg]),
               "L": lambda arg, p, w: (p, rotate(w, arg)),
               "R": lambda arg, p, w: (p, rotate(w, -arg)),
               "F": lambda arg, p, w: ([p[0]+arg*w[0], p[1]+arg*w[1]], w)}

pos = [0, 0]
wayPoint = [10, 1]

plt.scatter([pos[0]], [pos[1]], s=64, c="r")
history = [[pos[0]], [pos[1]]]
for move in moves:
    pos, wayPoint = instruction[move[0]](move[1], pos, wayPoint)
    if move[0] == "F":
        history[0].append(pos[0])
        history[1].append(pos[1])
print(pos, abs(pos[0])+abs(pos[1]))
plt.plot(history[0], history[1])
plt.scatter([pos[0]], [pos[1]], s=64, c="g")
plt.show()
