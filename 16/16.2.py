def multiply_departure_fields(input):
    rules = parse_rules(input[0])
    valid_tickets = find_valid_tickets(input[2], rules)
    determined_fields = match_fields(valid_tickets, rules)
    departures = 1
    my_ticket = input[1].split("\n")[1].split(",")
    for index, field in determined_fields.items():
        if "departure" in next(iter(field)):
            departures *= int(my_ticket[index])
    return departures
    
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

def find_valid_tickets(input, rules):
    valid = []
    for line in input.split("\n"):
        if line == "nearby tickets:":
            continue
        if is_valid_ticket(line, rules):
            valid.append(line)
    return valid

def is_valid_ticket(ticket, rules):
    for number in ticket.split(","):
        number = int(number)
        for acceptable in rules.values():
            if number in acceptable:
                break
        else:
            return False
    return True

def match_fields(tickets, rules):
    candidate_fields = {}
    for i in range(0, len(rules)):
        candidate_fields[i] = set(rules.keys())
    for ticket in tickets:
        for index, value in enumerate(ticket.split(",")):
            valid_candidates = set()
            for candidate in candidate_fields[i]:
                if int(value) in rules[candidate]:
                    valid_candidates.add(candidate)
            candidate_fields[index] = candidate_fields[index].intersection(valid_candidates)
    determined_fields = set()
    while len(candidate_fields) != sum([len(x) for x in candidate_fields.values()]):
        for fields in candidate_fields.values():
            if len(fields) == 1:
                determined_fields.add(next(iter(fields)))
        next_candidate_fields = candidate_fields.copy()
        for key, value in candidate_fields.items():
            if len(value) != 1:
                next_candidate_fields[key] = value - determined_fields
            else:
                next_candidate_fields[key] = value
        candidate_fields = next_candidate_fields
    return candidate_fields
input = open('16/input.txt').read().split("\n\n")
print(multiply_departure_fields(input))
