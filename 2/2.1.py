matches = 0
for line in open('2/input.txt'):
    acceptable_range, letter, password = line.split(" ")
    low, high = acceptable_range.split("-")
    count = password.count(letter[0])
    if count in range(int(low), int(high)+1):
        matches += 1
print(matches)