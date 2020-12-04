"""
Mandatory fields:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:

    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
Optional:
cid (Country ID)

Passport data is broken over a random number of lines,
but not broken in the middle of a value

Issues encountered:
1. Height value 92 (no unit suffix) - causes error
  Solution - could wrap in try/except, seems a little clunky but will catch all possible problems
  Should then probably also apply try/except to all validation functions
"""
import re

# Validation functions


def validate_birth_year(byr: str):
    return int(byr) >= 1920 and int(byr) <= 2002


def validate_issue_year(iyr: str):
    return int(iyr) >= 2010 and int(iyr) <= 2020


def validate_expiration_year(eyr: str):
    return int(eyr) >= 2020 and int(eyr) <= 2030


def validate_height(hgt: str):
    try:
        unit = hgt[-2:]
        value = int(hgt[:-2])
        if unit == 'cm':
            return value >= 150 and value <= 193
        elif unit == 'in':
            return value >= 59 and value <= 2030
        return False
    except:
        return False


hair_color_pattern = re.compile('^#[0-9a-f]{6}')


def validate_hair_color(hcl: str):
    return hair_color_pattern.match(hcl) != None


def validate_eye_color(ecl: str):
    if len(ecl) != 3:
        return False
    for match in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        if match == ecl:
            return True
    return False


passport_id_pattern = re.compile('^[0-9]{9}$')


def validate_passport_id(pid: str):
    return passport_id_pattern.match(pid) != None


# Python doesn't have switch statements so we use a map instead
rules_switch = {
    'byr': validate_birth_year,
    'iyr': validate_issue_year,
    'eyr': validate_expiration_year,
    'hgt': validate_height,
    'hcl': validate_hair_color,
    'ecl': validate_eye_color,
    'pid': validate_passport_id
}

fp = open('input', 'r')

# File small enough to read all at once
# Split on double newline to separate passports
passports = fp.read().split('\n\n')

valid_passports = 0
for passport in passports:
    # For more complex field validation, probably best to separate into key and value
    # Fields will be an array [[key, value], [key, value]]
    fields = [x.split(':') for x in passport.split()]
    print(fields)
    valid_fields = 0
    for field in fields:
        # Need to handle cid optional case
        if field[0] != 'cid':
            # Python doesn't have switch statements so we use a map instead
            if rules_switch[field[0]](field[1]):
                valid_fields += 1
            else:
                break  # Fail early if we find one invalid field
    if valid_fields == 7:
        valid_passports += 1

print(valid_passports)


fp.close()
