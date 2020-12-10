
with open("input.txt", "r") as f:
    numbers = [int(line) for line in f.readlines()]


def match(i):
    for j in range(i-25, i):
        for k in range(i-25, i):
            if j != k and numbers[j] + numbers[k] == numbers[i]:
                return True
    return False


for i in range(25, len(numbers)):
    if not match(i):
        key = numbers[i]
        print(key)  # answer 1
        break


for i in range(len(numbers)):
    key_list = [numbers[i]]
    key_sum = numbers[i]
    for j in range(i+1, len(numbers)):
        key_sum += numbers[j]
        key_list.append(numbers[j])
        if key_sum > key:
            break
        elif key_sum == key:
            print(min(key_list) + max(key_list))  # answer 2
            exit()
