def speak_the_numbers(starting_numbers, target):
    spoken_numbers = {}
    turn = 1
    for index, number in enumerate(starting_numbers):
        spoken_numbers[number] = turn
        turn += 1
    next_number = 0
    while True:
        if turn == target:
            return next_number
        try:
            last_spoken = spoken_numbers[next_number]                            
            last_number = next_number
            next_number = turn - last_spoken
        except KeyError:
            last_number = next_number
            next_number = 0
        spoken_numbers[last_number] = turn
        turn += 1

input = open('15/input.txt').read().split(",")
as_ints = [int(x) for x in input]
print(speak_the_numbers(as_ints, 2020))
print(speak_the_numbers(as_ints, 30000000))
