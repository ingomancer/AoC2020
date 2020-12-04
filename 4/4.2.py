import re
from itertools import takewhile

def check_height(x):
    val = int(''.join(takewhile(str.isdigit, x)))
    if "cm" in x:
        return val >= 150 and val <= 193
    elif "in" in x:
        return val >= 59 and val <= 76
    return False

def count_passports():
    required_fields = { "byr": lambda x: int(x) >= 1920 and int(x) <= 2002,
                        "iyr": lambda x: int(x) >= 2010 and int(x) <= 2020,
                        "eyr": lambda x: int(x) >= 2020 and int(x) <= 2030,
                        "hgt": check_height,
                        "hcl": lambda x: bool(re.match(r"#[0-9a-f]{6}", x)),
                        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                        "pid": lambda x: bool(re.match(r"^\d{9}$", x))}
    passports = []
    partial_passport = ""
    valid_passports = 0
    for line in open('4/input.txt'):
        if line.strip():
            partial_passport += line
        else:
            passports.append(partial_passport)
            partial_passport = ""
    passports.append(partial_passport)
    for passport in passports:
        valid_count = 0
        keys = []
        for entry in passport.split():
            key, value = entry.split(":")
            keys.append(key)
            if key == "cid":
                pass
            elif required_fields[key](value):
                valid_count += 1
        if valid_count == 7:
            if all([e in keys for e in required_fields.keys() ]):
                valid_passports += 1
    return valid_passports

print(count_passports())