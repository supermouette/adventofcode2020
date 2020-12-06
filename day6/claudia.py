with open("input.txt", "r") as f:
    customs = "".join(f.readlines()).split("\n\n")
    print(sum([len({c for c in ''.join(custom.split('\n'))}) for custom in customs]))  # part 1

    s = 0
    a = {1, 2}
    for custom in customs:
        passengers = custom.split("\n")
        all_yes = set(passengers[0])
        for i in range(1, len(passengers)):
            current_yes = set(passengers[i])
            tmp_yes = all_yes.copy()
            for character in all_yes:
                if character not in current_yes:
                    tmp_yes.remove(character)
            all_yes = tmp_yes
        s += len(all_yes)
    print(s)  # part 2
