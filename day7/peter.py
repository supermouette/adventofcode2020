import re

with open("input.txt", "r") as f:
    lines = f.readlines()
    colors = {}
    for line in lines:
        splited = line.split(" ")
        color = " ".join(splited[:2])
        contains = " ".join(splited[4:]).replace(",", ".").split(".")[:-1]
        component_list = []
        for e in contains:
            if e[0] == " ":
                e = e[1:]
            if e[:2] == "no":
                break
            component_list.append([e.split(' ')[0], " ".join(e.split(' ')[1:3])])
        colors[color] = component_list


def contain_shiny_gold(color, contain):
    if color == "shiny gold":
        return True
    else:
        for nb, c in contain:
            if contain_shiny_gold(c, colors[c]):
                return True
        return False


s = 0
for color in colors.keys():
    if contain_shiny_gold(color, colors[color]):
        s += 1
print(s-1)  # answer 1


def count_bag(color, contain):
    if len(contain) == 0:
        return 0
    else:
        return sum([int(nb) + int(nb)*count_bag(c, colors[c])for nb, c in contain])


print(count_bag("shiny gold", colors["shiny gold"]))
