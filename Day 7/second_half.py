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
# and a value that's another dictionary with the bags that should be contained within it
# as keys and the number of those bags that should be contained as values
rules = {
    rule.strip(): {bag_amount.strip()[1:].strip() : int(bag_amount.strip()[0]) for bag_amount in contents.strip().split(",") if bag_amount != "no other" }
    for rule, contents in [
            line[:-1].split("contain") for line in RAW_DATA.replace("bags", "bag").replace("bag", "").split("\n")
        ]
    }

def recurse(bag_type):
    """For the provided bag type, count the bags
    contained in it by adding the amount of bags for each
    type and the bags contained within (repeat the process for inner bags
    until a bag that contains no other bags is reached)
    """
    rule = rules[bag_type]
    bags_within = 0
    if rule == {}:
        return 0
    for contained_bag in rule.keys():
        bags_within += rule[contained_bag] + rule[contained_bag] * recurse(contained_bag)
    return bags_within

print(recurse('shiny gold'))
