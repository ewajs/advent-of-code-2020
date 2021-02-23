from raw_data import RAW_DATA

lines = [line.strip() for line in RAW_DATA.strip().split("\n")]

def first_half(right, down):
    x = 0
    y = 0
    trees = 0
    while y < len(lines):
        if lines[y][x % len(lines[y])] == '#':
            trees +=1
        x += right
        y += down
    
    return trees

def second_half():
    # (RIGHT, DOWN)
    SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for right, down in SLOPES:
        print(first_half(right, down))
        total *= first_half(right, down)
    return total

print(first_half(3, 1))

print(second_half())
