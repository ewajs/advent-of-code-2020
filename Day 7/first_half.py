from raw_data import RAW_DATA

test_data = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".strip()

# Compute the rules so as to have an dictionary with starting bag as a key
# and a list with the bags that should be contained within it
# for the first half, amount of bags is not required and is removed
# by splicing out the first character unless the rule says no other (as that's not a bag type)
rules = {
    rule.strip(): [allowable.strip()[1:].strip() if allowable != "no other" else "no other" for allowable in contents.strip().split(",")] 
    for rule, contents in [
            line[:-1].split("contain") for line in RAW_DATA.replace("bags", "bag").replace("bag", "").split("\n")
        ]
    }

def recurse(bag_types):
    """For each bag type, make a set of bags that can contain
    them. If there are bags that could contain the current one
    repeat the process for that bag type adding in the already
    found bag types. If there are no bags that can contain the 
    current one, then return an empty set so the recursion finishes
    and the final output is a set with all bags that could eventually
    contain the starting bag(s).
    """
    bags_that_can_contain = set()
    for bag_type in bag_types:
        for containing_bag, containable_bags in rules.items():
            if bag_type in containable_bags:
                bags_that_can_contain.add(containing_bag)
    # print(f'{bag_type} can be contained in {bags_that_can_contain}')
    if bags_that_can_contain:
        return recurse(bags_that_can_contain) | bags_that_can_contain
    else:
        return set()

 

print(len(recurse({'shiny gold'})))