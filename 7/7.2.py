def bag_options():
    rules = {}
    for line in open('7/input.txt'):
        outer_bag, contents = line.strip().split("contain")
        outer_bag = outer_bag.strip().rstrip("s")
        rules[outer_bag] = {}
        for bags in contents.strip(".").split(","):
            if bags[1] == 'n':
                continue
            rules[outer_bag][bags[2:].strip().rstrip("s")] = bags[1]
    return rules

def count_bags(bag, rules):
    sum = 0
    for bag, count in rules[bag].items():
        sum += int(count) + count_bags(bag, rules)*int(count)
    return sum
    
print(count_bags("shiny gold bag", bag_options()))