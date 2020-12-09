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
            return numbers[i]
    

numbers = open('9/input.txt').read().splitlines()
print(find_unsum(numbers, 25))