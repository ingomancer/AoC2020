def count_answers():
    answers = []
    group = 0
    group_answers = []
    sum = 0
    for line in open('6/input.txt'):
        if line.strip():
            for answer in line.strip():
                group_answers.append(answer)
        else:
            answers.append(group_answers)
            group_answers = []
            group += 1
    answers.append(group_answers)

    for group_answer in answers:
        sum += len(list(set(group_answer)))
    return sum
print(count_answers())