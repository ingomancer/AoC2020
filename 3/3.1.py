def count_trees():
    pos = 0
    trees = 0
    for line in open('3/input.txt'):
        if line[pos] == "#":
            trees += 1

        pos = (pos + 3) % len(line.rstrip())
    return trees

print(count_trees())