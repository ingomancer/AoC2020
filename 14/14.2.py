from collections import defaultdict
from itertools import product

def do_the_needful(input):
    mem = defaultdict(int)
    mask = ""
    for line in input:
        action, value = line.split(" = ")
        if action == "mask":
            mask = value
        else:
            index = action[4:-1]
            index = bin(int(index))[2:]
            index = list(index.zfill(36))
            floaty_bois = 0
            for i in range(len(mask)):
                if mask[i] == "1":
                    index[i] = mask[i]    
                elif mask[i] == "X":
                    floaty_bois += 1
                    index[i] = "X"
            indices = []
            for combination in product(range(2), repeat=floaty_bois):
                indices.append(modify_index("".join(index), combination))
            for new_index in indices:
                mem[int("0b"+new_index, 2)] = int(value)
    return sum(mem.values())

def modify_index(index, combination):
    for value in combination:
        index = index.replace("X", str(value), 1)
    return index

input = open('14/input.txt').read().splitlines()
print(do_the_needful(input))