from time import time
t0 = time()
numbers = [1, 17, 0, 10, 18, 11, 6]
n = 2020  # part 1
n = 30000000  # part 2

size = len(numbers)

n_dict = {numbers[i]: i + 1 for i in range(size)}
prev = numbers[-1]
while size != n:
    if prev in n_dict:
        new_num = size - n_dict[prev]
    else:
        new_num = 0
    n_dict[prev] = size
    size += 1
    prev = new_num

print(new_num)
print(time()-t0)
