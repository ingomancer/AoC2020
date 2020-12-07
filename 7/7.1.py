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

def find_outer_bags(bag, rules):
    outer_bags = []
    for key, value in rules.items():
        if bag in value:
            outer_bags.append(key)
    if not outer_bags:
        return []
    lower_bags = []
    for outer_bag in outer_bags:
        lower_bags.extend(find_outer_bags(outer_bag, rules))
    outer_bags.extend(lower_bags)
    return list(set(outer_bags))


print(len(find_outer_bags("shiny gold bag", bag_options())))