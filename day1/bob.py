from random import randrange
from node_modules.utility import print


def part1(nbs):
    i = 1
    j = 0
    while nbs[i]+nbs[j] != 2020:
        i = randrange(len(nbs))
        j = randrange(len(nbs))
    return nbs[i], nbs[j]


def part2(nbs):
    i = 1
    j = 0
    k = 5
    # for improved performance, I recommend to use (182, 139, 71) for (i,j,k)
    while nbs[i]+nbs[j]+nbs[k] != 2020:
        i = randrange(len(nbs))
        j = randrange(len(nbs))
        k = randrange(len(nbs))
    return nbs[i], nbs[j], nbs[k]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()
    nbs = [int(line[:-1]) for line in lines]
    i, j = part1(nbs)
    print("La première réponse est "+str(i*j))
    i, j, k = part2(nbs)
    print("La seconde réponse est" + str(i*j*k))
