from collections import deque

def parse_rules(input):
    rules = {}
    for line in input:
        rule_no, rule = line.split(":")
        rules[rule_no] = rule.strip().strip('"')
    rule_list = build_list(rules, '0')
    rule_strings = explode_list(rule_list)

def build_list(rules, key):
    rule_list = []
    pipe = False
    sublist = []
    for rule in rules[key].split(" "):
        if rule == "|":
            pipe = True
            pipelist = [sublist]
            sublist = []
        elif rule == "a" or rule == "b":
            sublist.append([rule])
        else:
            sublist.extend(build_list(rules, rule))
    if pipe:
        pipelist.append(sublist)
        rule_list.extend(pipelist)
    else:
        rule_list.extend(sublist)
    return rule_list

def explode_list(rule_list):
    strings = [""]
    for entry in rule_list:
        entries = len(entry)
        if entries == 1:
            new_strings = []
            for rule in strings:
                rule += entry[0]
                new_strings.append(rule)
            strings = new_strings
        else:
            new_strings = []
            for i in range(entries):
                new_strings.extend(strings)
            strings = new_strings
    print(strings)


input = open('19/input.txt').read().splitlines()
print(parse_rules(input))
