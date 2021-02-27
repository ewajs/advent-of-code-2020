from raw_data import RAW_DATA

seats = [line.strip() for line in RAW_DATA.split("\n")]
# Encoding of seats is simply a 2-D binary value where
# Vertically: F = 0, B = 1
# Horizontally: L = 0, R = 1

# (This can of course be done with a single LC doing all operations in one go)
ids = [
# Compute IDs (Row * 8 + Col) and return max
row * 8 + col for row, col in [
    # Compute Row and Col in base 10
    (int(vert.replace("F", "0").replace("B", "1"), 2), int(hor.replace("L", "0").replace("R", "1"), 2)) for hor, vert in [
        # Split line into Row and Col Codes
        (line[-3:], line[:-3]) for line in seats
        ]
    ]
]



def first_half():
    return max(ids)


def second_half():
    sorted_ids = sorted(ids)
    prev = sorted_ids[0]
    for bid in sorted_ids[1:]:
        if bid - prev == 2:
            return bid - 1
        prev = bid
    


print(first_half())
print(second_half())