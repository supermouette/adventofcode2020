with open("input.txt", "r") as f:
    seats = [int(s[:-1].replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for s in f.readlines()]
    seats.sort()
    print(seats[-1])  # answer 1
    for i in range(1, len(seats)):
        if seats[i] - seats[i-1] == 2:
            print(seats[i]-1)  # answer 2
            break
