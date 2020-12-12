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
    waypoint_x = 1
    waypoint_y = 10
    cur_x = 0
    cur_y = 0
    facing = 0
    for instruction in input:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "F":
            cur_x += waypoint_x*value
            cur_y += waypoint_y*value
        elif action == "R":
            for i in range(0, value // 90):
                waypoint_x, waypoint_y = (-waypoint_y, waypoint_x)
        elif action == "L":
            for i in range(0, value // 90):
                waypoint_x, waypoint_y = (waypoint_y, -waypoint_x)
        else:
            waypoint_x += directions[action][0]*value
            waypoint_y += directions[action][1]*value
    return abs(cur_x) + abs(cur_y)        


input = open('12/input.txt').read().splitlines()
print(travel(input))