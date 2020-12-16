#  data loading
with open("input.txt", "r") as f:
    rules, my_ticket, tickets = "".join(f.readlines()).split("\n\n")

_rules = rules.split("\n")
my_ticket = [int(val) for val in my_ticket.split("\n")[1].split(',')]
tickets = [[int(val) for val in t.split(',')] for t in tickets.split("\n")[1:-1]]

rules = {}
for r in _rules:
    name, values = r.split(":")
    ranges = values.split(" or ")
    ranges = [ra.split("-") for ra in ranges]
    min_i = int(ranges[0][0])
    max_i = int(ranges[0][1])
    min_j = int(ranges[1][0])
    max_j = int(ranges[1][1])
    rules[name] = lambda x, min_i=min_i, max_i=max_i, min_j=min_j, max_j=max_j: \
        min_i <= x <= max_i or min_j <= x <= max_j

# question 1

sum = 0
valid = []
for t in tickets:
    for field in t:
        for r in rules:
            if rules[r](field):
                break
        else:
            sum += field
            break
    else:
        valid.append(t)
print(sum)  # answer 1

# question 2
order = []
all_tickets = [my_ticket] + valid

for i in range(len(my_ticket)):
    possible_rules = list(rules.keys())
    tmp_pr = possible_rules[:]
    for t in all_tickets:
        for pr in possible_rules:
            if not rules[pr](t[i]):
                tmp_pr.remove(pr)
        possible_rules = tmp_pr
    order.append(possible_rules)

final_order = {}
while len(final_order) != len(my_ticket):
    for i in range(len(order)):
        o_tmp = order[i][:]
        for key in order[i]:
            if key in final_order:
                o_tmp.remove(key)
        order[i] = o_tmp
        if len(order[i]) == 1:
            final_order[order[i][0]] = i


sum = 1
for field in final_order:
    if field.startswith("departure"):
        sum *= my_ticket[final_order[field]]
print(sum)
