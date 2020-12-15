from math import ceil, inf

def next_bus(timestamp, busses):
    nearest_bus = inf
    id = 0
    for bus in busses.split(","):
        if bus == "x":
            continue
        bus = int(bus)
        next_departure = ceil(timestamp/bus)*bus
        if next_departure < nearest_bus:
            nearest_bus = next_departure
            id = bus
    return (nearest_bus - timestamp)*id

input = open('13/input.txt').read().splitlines()
timestamp = int(input[0])
busses = input[1]
print(next_bus(timestamp, busses))