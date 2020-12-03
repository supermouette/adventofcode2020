from functools import reduce


with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [line[:-1] for line in lines]

slope = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = []
for r, d in slope:  # right, down
    trees.append(0)
    for i in range(0, len(lines), d):
        trees[-1] += lines[i][(r*i//d) % len(lines[i])] == "#"
print(trees)
print("answer 1", trees[1])
print("answer 2", reduce(lambda x, y: x*y, trees))
