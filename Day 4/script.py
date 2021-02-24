from raw_data import RAW_DATA
import string
import sys

def to_dict(a_list):
    """Takes in a list of k:v and returns a dict"""
    return {k: v for k, v in [item.split(":") for item in a_list]}

def validate_passport(passport):
    if not REQUIRED_FIELDS_SET.issubset(set(passport.keys())):
        return False
    try:
        conditions = [
            passport['byr'].isnumeric() and 1920 <= int(passport['byr']) <= 2002,
            passport['iyr'].isnumeric() and 2010 <= int(passport['iyr']) <= 2020,
            passport['eyr'].isnumeric() and 2020 <= int(passport['eyr']) <= 2030,
            passport['hgt'][-2:] in ('cm', 'in') and passport['hgt'][:-2].isnumeric() and (150 <= int(passport['hgt'][:-2]) <= 193 if passport['hgt'][-2:] == 'cm' else 59 <= int(passport['hgt'][:-2]) <= 76),
            passport['hcl'][0] == '#' and all(letter in string.hexdigits.lower() for letter in passport['hcl'][1:]),
            passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            passport['pid'].isnumeric() and len(passport['pid']) == 9
        ]
    except:
        print(passport)
        print(sys.exc_info())
        exit()
    

    return all(conditions) 

data =[ 
    to_dict(metadata)
    for metadata in [
        " ".join(passport.split("\n")).split(" ") 
        for passport in RAW_DATA.strip().split("\n\n")
        ]
    ]

# cid is optional
REQUIRED_FIELDS_SET = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def first_half():
    return sum([REQUIRED_FIELDS_SET.issubset(set(item.keys())) for item in data])

def second_half():
    return sum([validate_passport(passport) for passport in data])
    


print(second_half())