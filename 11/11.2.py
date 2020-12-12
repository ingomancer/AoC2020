floor = "."
empty = "L"
occupied = "#"

def find_fixpoint(state):
    prev_state = state
    next_state = get_next_state(state)
    count = 0
    while next_state != prev_state:
        count += 1
        prev_state = next_state
        next_state = get_next_state(prev_state)
    return count_seats(next_state, occupied)

def get_next_state(state):
    next_state = []
    for i in range(len(state)):
        sublist = []
        for j in range(len(state[i])):
            neighbours = count_visibly_occupied(state, i, j)
            if state[i][j] == floor:
                sublist.append(floor)
            elif state[i][j] == empty:
                if neighbours == 0:
                    sublist.append(occupied)
                else:
                    sublist.append(empty)
            else:
                if neighbours >= 5:
                    sublist.append(empty)
                else:
                    sublist.append(occupied)
        next_state.append(sublist)
    return next_state

directions = [
    [-1, 0], # up
    [1, 0], # down 
    [0, -1], # left 
    [0, 1], # right
    [-1, -1], # up left 
    [-1, 1], # up right 
    [1, -1], # down left 
    [1, 1], # down right
]

def count_visibly_occupied(state, x, y):
    count = 0
    for direction in directions:
        count += look_in_direction(state, *direction, x, y)
    return count

def look_in_direction(state, delta_x, delta_y, x, y):
    x += delta_x
    y += delta_y
    while 0 <= x < len(state) and 0 <= y < len(state[x]):
        if state[x][y] == occupied:
            return 1
        elif state[x][y] == empty:
            return 0
        x += delta_x
        y += delta_y
    return 0

def count_seats(state, seat):
    count = 0
    for i in state:
        for j in i:
            count += 1 if j == seat else 0
    return count

input = open('11/input.txt').read().splitlines()
print(find_fixpoint(input))