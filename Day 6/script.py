from raw_data import RAW_DATA
from functools import reduce

def first_half():
    
    # Split in groups, make a set of each group's answers (eliminate duplicates) and 
    # sum the length of each set together
    return sum([len(set(group.replace("\n", ""))) for group in RAW_DATA.split("\n\n")])

def second_half():
    # Split in groups and re-split into answers, for each list of answers 
    # in a group, make it a set, then compute the intersection of all sets 
    # in a given group to find the answers to which everyone replied yes to. 
    # Compute the length of each of these sets and sum them together.
    return sum([len(reduce(lambda x, y: x & y, map(set, group))) for group in
            [group.split("\n") for group in RAW_DATA.split("\n\n")]
        ])

print(second_half())