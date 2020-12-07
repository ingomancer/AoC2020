from collections import defaultdict

def count_answers():
    answers = []
    group = 0
    group_answers = defaultdict(int)
    sum = 0
    for line in open('6/input.txt'):
        if line.strip():
            for answer in line.strip():
                group_answers[answer] += 1
            group_answers['people'] += 1
        else:
            answers.append(group_answers)
            group_answers = defaultdict(int)
            group += 1
    answers.append(group_answers)
    for group_answer in answers:
        all_answered = []
        for key, value in group_answer.items():
            if key == 'people':
                continue
            if value == group_answer['people']:
                all_answered.append(key)
        sum += len(list(set(all_answered)))
        all_answered = []
    return sum
print(count_answers())