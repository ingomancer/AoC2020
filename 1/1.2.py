entries = []
for line in open('1/input.txt'):
    entries.append(int(line))

for i in entries:
    for j in entries:
        for k in entries:
            if i+j+k == 2020:
                print(i*j*k)