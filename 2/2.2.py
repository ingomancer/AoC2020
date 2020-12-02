matches = 0
for line in open('2/input.txt'):
    acceptable_positions, letter, password = line.split(" ")
    low, high = acceptable_positions.split("-")
    if (letter[0] == password[int(low)-1] ) != (letter[0] == password[int(high)-1]):
        matches += 1
print(matches)