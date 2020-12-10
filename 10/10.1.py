from collections import defaultdict

def joltage_differences(numbers):
    diffs = defaultdict(int)
    prev_jolt = 0
    numbers = sorted(numbers)
    numbers.append(numbers[-1] + 3)
    for adapter in numbers:
        diffs[adapter - prev_jolt] += 1
        prev_jolt = adapter
    return diffs[1] * diffs[3]

input = open('10/input.txt').read().splitlines()
numbers = [int(x) for x in input]
print(joltage_differences(numbers))