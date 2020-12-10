from functools import reduce

def valid_configurations(numbers):
    partitions = []
    permutations = []
    last_split = 0
    for i in range(len(numbers)-1):
        if numbers[i+1] - numbers[i] == 3:
            partitions.append(numbers[last_split:i+1])
            last_split = i+1
        
    for sublist in partitions:
        sublists = find_valid_shorter(sublist)
        permutations.append(len(sublists)+1)        
    return reduce(lambda a,b: a*b, permutations)

def find_valid_shorter(numbers):
    tried_list = []
    for i in range(1, len(numbers) - 1):
        sublist = [x for x in numbers if x != numbers[i]]
        if check_valid(sublist):
            if sublist not in tried_list:
                tried_list.append(sublist)
    sublists = []
    for sublist in tried_list:
        sublists += find_valid_shorter(sublist)
    for sublist in sublists:
        if sublist not in tried_list:
            tried_list.append(sublist)
    return tried_list

def check_valid(numbers):
    last = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] - last > 3:
            return False
        last = numbers[i]
    return True
    
input = open('10/input.txt').read().splitlines()
numbers = [int(x) for x in input]
numbers.append(0)
numbers = sorted(numbers)
numbers.append(numbers[-1]+3)
print(valid_configurations(numbers))