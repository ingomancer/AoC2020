directions = {
    "E": [0, 1],
    "S": [-1, 0],
    "W": [0, -1],
    "N": [1, 0],
}

cardinal = {
    0: "E",
    1: "S",
    2: "W",
    3: "N",
}

def travel(input):
    cur_x = 0
    cur_y = 0
    facing = 0
    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "F":
            cur_x += directions[cardinal[facing]][0]*value
            cur_y += directions[cardinal[facing]][1]*value
        elif action == "R":
            facing = (facing + (value / 90)) % 4
        elif action == "L":
            facing = (facing - (value / 90)) % 4
        else:
            cur_x += directions[action][0]*value
            cur_y += directions[action][1]*value
    return abs(cur_x) + abs(cur_y)        


input = open('12/input.txt').read().splitlines()
print(travel(input))