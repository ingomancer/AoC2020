def find_unsum(numbers, preamble_length):
    preamble = []
    for i in range(preamble_length):
        preamble.append(int(numbers[i]))
    for i in range(preamble_length, len(numbers)):
        sums = []
        for p1 in range(len(preamble)):
            for p2 in range(p1+1, len(preamble)):
                sums.append(preamble[p1] + preamble[p2])
        if int(numbers[i]) in sums:
            preamble.append(int(numbers[i]))
            preamble.pop(0)
        else:
            return int(numbers[i])
    
def find_sum(numbers, target):
    i = 0
    j = 1
    while True:
        sum = 0
        for p in range(i, j):
            sum += int(numbers[p])
        if sum == target:
            return i, j
        elif sum < target:
            j += 1
        else:
            i += 1

input = open('9/input.txt').read().splitlines()
numbers = [int(x) for x in input]
target = find_unsum(numbers, 25)
i, j = find_sum(numbers, target)
print(int(max(numbers[i:j])) + int(min(numbers[i:j])))