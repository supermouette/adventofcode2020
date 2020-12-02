with open("input.txt", "r") as f:
    print(sum([int(l.split(' ')[0].split('-')[0]) <= l.split(' ')[2].count(l.split(' ')[1][0]) <= int(l.split(' ')[0].split('-')[1]) for l in f.readlines()]))

