with open("input.txt", "r") as f:
    lines = [line.split(" ") for line in f.readlines()]


def execute(lines):
    acc = 0
    visited = set()
    i = 0
    while i not in visited and i+1 != len(lines):
        visited.add(i)
        if lines[i][0] == "jmp":
            i += int(lines[i][1])
        else:
            if lines[i][0] == "acc":
                acc += int(lines[i][1])
            i += 1
    return i, acc, visited


def swap(line):
    if line[0] == "jmp":
        line[0] = "nop"
    else:
        line[0] = "jmp"


if __name__ == "__main__":
    i, acc, visited = execute(lines)
    print(i, acc, len(visited))  # answer 1 is acc

    line_to_swap = [i for i in visited if lines[i][0] != "acc"]
    # print(len(line_to_swap))  # in my case, max 87 swap to execute
    # print(len([line for line in lines if line[0] != "acc"]))  # out of curiosity, there is 290 lines with jmp or nop

    for to_swap in line_to_swap:
        swap(lines[to_swap])
        i, acc, visited = execute(lines)
        swap(lines[to_swap])
        if i+1 == len(lines):
            print(i, acc, len(visited))
            print(lines[to_swap])
            break




