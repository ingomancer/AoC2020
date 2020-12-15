from collections import defaultdict

def do_the_needful(input):
    mem = defaultdict(int)
    mask = ""
    for line in input:
        action, value = line.split(" = ")
        if action == "mask":
            mask = value
        else:
            index = action[4:-1]
            value = bin(int(value))[2:]
            value = list(value.zfill(36))
            for i in range(len(mask)):
                if mask[i] != "X":
                    value[i] = mask[i]            
            mem[index] = int("0b" + "".join(value), 2)
    return sum(mem.values())

input = open('14/input.txt').read().splitlines()
print(do_the_needful(input))