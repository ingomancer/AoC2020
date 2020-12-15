from math import ceil, inf

def find_magical_time(busses):
    time = 13
    increment = 13
    bus_and_offset_found = {}
    for index, bus in enumerate(busses):
        if index == 0:
            continue
        if bus != "x":
            bus_and_offset_found[int(bus)] = (index, False)
    while True:
        for bus, data in bus_and_offset_found.copy().items():
            bus = int(bus)
            if not data[1]:
                if (time + data[0]) % bus == 0:
                    bus_and_offset_found[bus] = (data[0], True)
                    increment *= bus
        if (all([x[1] for x in bus_and_offset_found.values()])):
            return time
        time += increment


input = open('13/input.txt').read().splitlines()
busses = input[1].split(",")
print(find_magical_time(busses))