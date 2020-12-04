with open("input.txt", "r") as f:
    passports = "".join(f.readlines()).split("\n\n")
# part 1
toMatch = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
print(sum([sum([i.split(":")[0] in toMatch for i in p.replace("\n", " ").split(" ")]) == 7 for p in passports]))

# part 2
import re 

toMatch = {"byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
           "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
           "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
           "hgt": lambda x: (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),
           "hcl": lambda x: bool(re.search(r"^#[0-9a-f]{6}$", x)),
           "ecl": lambda x: x in "amb blu brn gry grn hzl oth".split(" "),  # I will not make a list by myself
           "pid": lambda x: bool(re.search(r"^[0-9]{9}$", x))}

print(sum([sum([toMatch[i.split(":")[0]](i.split(':')[1]) for i in p.replace("\n", " ").split(" ") if i.split(":")[0] in toMatch.keys()]) == 7 for p in passports]))
