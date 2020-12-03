def count_trees(go_right, go_down):
    pos = 0
    trees = 0
    linecount = 0
    for line in open('3/input.txt'):
        if linecount % go_down == 1:
            linecount += 1
            continue
        if line[pos] == "#":
            trees += 1

        pos = (pos + go_right) % len(line.rstrip())
        linecount += 1
    return trees

oneone = count_trees(1, 1)
threeone = count_trees(3, 1)
fiveone = count_trees(5, 1)
sevenone = count_trees(7, 1)
onetwo = count_trees(1, 2)

print(oneone)
print(threeone)
print(fiveone)
print(sevenone)
print(onetwo)
print(oneone * threeone * fiveone * sevenone * onetwo)