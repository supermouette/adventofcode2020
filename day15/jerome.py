from time import time
t0 = time()
numbers = [1, 17, 0, 10, 18, 11, 6]
n = 2020  # part 1
n = 30000000  # part 2

n_dict = {numbers[i]: i for i in range(len(numbers))}

while len(numbers) != n:
    prev = numbers[-1]
    if prev in n_dict:
        id = len(numbers)-1 - n_dict[prev]
    else:
        id = 0
    n_dict[prev] = len(numbers) - 1
    numbers.append(id)

print(numbers[-1])
print(time()-t0)
