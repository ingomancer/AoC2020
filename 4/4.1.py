def count_passports():
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
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
        keys = []
        for entry in passport.split():
            key = entry.split(":")[0]
            keys.append(key)
        if all([e in keys for e in required_fields]):
            valid_passports += 1
    return valid_passports

print(count_passports())