def part1(nbs):
    for i in nbs:
        for j in nbs:
            if i+j == 2020:
                return i, j


def part2(nbs):
    for i in nbs:
        for j in nbs:
            if i+j < 2020:  # useless
                for k in nbs:
                    if i+j+k == 2020:
                        return i, j, k


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    nbs = [int(line[:-1]) for line in lines]
    i, j = part1(nbs)
    print("La première réponse est "+str(i*j))
    i, j, k = part2(nbs)
    print("La seconde réponse est" + str(i*j*k))
