with open("input.txt", "r") as f:
    print(sum([(l.split(' ')[2][-1 + int(l.split(' ')[0].split('-')[0])] == l.split(' ')[1][0]) ^ (l.split(' ')[2][-1 + int(l.split(' ')[0].split('-')[1])] == l.split(' ')[1][0]) for l in f.readlines()]))

