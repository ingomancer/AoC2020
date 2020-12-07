def get_seat():
    ids = []
    for line in open('5/input.txt'):
        row_min = 0
        row_max = 127
        seat_min = 0
        seat_max = 7
        for char in line:
            if char == "F":
                row_max -= (row_max - row_min + 1)//2
            elif char == "B":
                row_min += (row_max - row_min + 1)//2
            elif char == "L":
                seat_max -= (seat_max - seat_min + 1)//2
            elif char == "R":
                seat_min += (seat_max - seat_min + 1)//2
            else:
                pass
        id = row_min * 8 + seat_min
        ids.append(id)
    ids = sorted(ids)
    for i in range(1, 1024):
        if i not in ids:
            if i-1 in ids and i+1 in ids:
                print(i)

print(get_seat())