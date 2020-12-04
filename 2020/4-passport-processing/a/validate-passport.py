"""
Mandatory fields:
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
Optional:
cid (Country ID)

Passport data is broken over a random number of lines,
but not broken in the middle of a value
"""

fp = open('input', 'r')

# File small enough to read all at once
# Split on double newline to separate passports
passports = fp.read().split('\n\n')

valid_passports = 0
for passport in passports:
    fields = passport.split()
    # print(fields)
    valid_fields = 0
    for field in fields:
        if field[:3] != 'cid':  # Ignore cid field
            valid_fields += 1  # Assumes that we won't have invalid field names
    if valid_fields == 7:
        valid_passports += 1

print(valid_passports)


fp.close()
