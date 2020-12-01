entries = []
for line in open('1/input.txt'):
    entries.append(int(line))

for i in entries:
    for j in entries:
        if i + j == 2020:
            print(i*j)