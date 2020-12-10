with open("input.txt", "r") as f:
    adapters = [int(line) for line in f.readlines()]
adapters.sort()
diffs = {1: 1, 3: 1}
for i in range(1, len(adapters)):
    diffs[adapters[i]-adapters[i-1]] += 1
print(diffs, diffs[3]*diffs[1])  # answer 1

possible_jumps = {0: [i for i in adapters[:3] if i < 4]}
# print(adapters)
for i in range(len(adapters)):
    possible_jumps[adapters[i]] = [a for a in adapters[i+1:i+4] if a < adapters[i]+4]
# print(possible_jumps)

nbs_jump = {}


def count_way(adapter):
    if len(possible_jumps[adapter]) == 0:
        return 1
    elif adapter in nbs_jump:
        return nbs_jump[adapter]
    else:
        product = 0
        for jump in possible_jumps[adapter]:
            product += count_way(jump)
        nbs_jump[adapter] = product
        return product


print(count_way(0))  # answer 2

