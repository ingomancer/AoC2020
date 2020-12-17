from collections import defaultdict

def simulate_cubes(input, cycles):
    active_cubes = create_cubes(input)
    for _ in range(cycles):
        cubes_to_consider = set()
        for cube in active_cubes.keys():
            cubes_to_consider.add(cube)
            neighbours = cube_neighbours(cube)
            for neighbour in neighbours:
                cubes_to_consider.add(neighbour)
        active_cubes_next = defaultdict(bool)
        for cube in cubes_to_consider:
            active_neighbours = sum([active_cubes[x] for x in cube_neighbours(cube)])
            if active_cubes[cube]:
                if 2 <= active_neighbours <= 3:
                    active_cubes_next[cube] = True
            else:
                if active_neighbours == 3:
                    active_cubes_next[cube] = True
        active_cubes = active_cubes_next
    return len(active_cubes)
        
def cube_neighbours(cube):
    x,y,z = cube
    neighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx == dy == dz == 0:
                    continue
                neighbours.append((x+dx,y+dy,z+dz))
    return neighbours

def create_cubes(input):
    cubes = defaultdict(bool)
    y = 0
    z = 0
    for line in input:
        x = 0
        for cube in line:
            if cube == "#":
                cubes[(x,y,z)] = True
            x += 1
        y += 1
    return cubes


input = open('17/input.txt').readlines()
print(simulate_cubes(input, 6))