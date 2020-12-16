def sum_invalid_fields(input):
    rules = parse_rules(input[0])
    invalid_fields = find_invalid_fields(input[2], rules)
    return sum(invalid_fields)

def parse_rules(input):
    rules = {}
    for line in input.split("\n"):
        name, ranges = line.split(": ")
        ranges = ranges.split(" or ")
        valid_numbers = []
        for rule in ranges:
            start, stop = rule.split("-")
            valid_numbers += list(range(int(start), int(stop)+1))
        rules[name] = valid_numbers
    return rules

def find_invalid_fields(input, rules):
    invalid = []
    for line in input.split("\n"):
        if line == "nearby tickets:":
            continue
        for number in line.split(","):
            number = int(number)
            for acceptable in rules.values():
                if number in acceptable:
                    break
            else:
                invalid.append(number)
    return invalid


input = open('16/input.txt').read().split("\n\n")
print(sum_invalid_fields(input))