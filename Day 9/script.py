from raw_data import RAW_DATA, TEST_DATA

PREAMBLE_LENGTH = 25

data = [int(num) for num in RAW_DATA.split("\n")]



def check_valid(index):
    for i in range(index - PREAMBLE_LENGTH, len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == data[index]:
                return True
    return False

def first_half():
    for index, value in enumerate(data[PREAMBLE_LENGTH:], start=PREAMBLE_LENGTH):
        print(f"Checking index {index} with value {value}")
        if not check_valid(index):
            return value
    return "No value found"

# First Half
print(first_half())

# Second Half


def find_contiguous_set():
    num = first_half()
    # Up until the second to last pick the index
    for start_index in range(len(data) - 1):
        for stop_index in range(start_index + 1, len(data)):
            cumsum = sum(data[start_index:stop_index + 1])
            if cumsum == num:
                # Found contiguous set
                return data[start_index:stop_index + 1]
            if cumsum > num:
                # Exceeded number, no point in keep trying with this start_index
                break

def second_half():
    contiguous_set = find_contiguous_set()
    return max(contiguous_set) + min(contiguous_set)

print(second_half())
    

