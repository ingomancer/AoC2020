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
            neighbours = count_neighbours(state, i, j)
            if state[i][j] == floor:
                sublist.append(floor)
            elif state[i][j] == empty:
                if neighbours == 0:
                    sublist.append(occupied)
                else:
                    sublist.append(empty)
            else:
                if neighbours >= 4:
                    sublist.append(empty)
                else:
                    sublist.append(occupied)
        next_state.append(sublist)
    return next_state
            
def count_neighbours(state, x, y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if ((x != i or y != j) 
            and 0 <= i < len(state) 
            and 0 <= j < len(state[i])):
                if state[i][j] == occupied:
                    count += 1
    return count

def count_seats(state, seat):
    count = 0
    for i in state:
        for j in i:
            count += 1 if j == seat else 0
    return count

input = open('11/input.txt').read().splitlines()
print(find_fixpoint(input))