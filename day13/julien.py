with open("input.txt", "r") as f:
    lines = f.readlines()

arrival = int(lines[0].strip("\n"))
buses = [int(bus) for bus in lines[1].strip("\n").split(",") if bus != "x"]

print(arrival, buses)
min_time = buses[0] - arrival % buses[0]
min_bus = buses[0]
for bus in buses:
    if bus - arrival % bus < min_time:
        min_time = bus - arrival % bus
        min_bus = bus

print(min_time, min_bus, min_time*min_bus)
