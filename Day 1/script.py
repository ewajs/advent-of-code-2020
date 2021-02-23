from raw_data import RAW_DATA
# List Comprehension to process the data
data = [int(i.strip()) for i in  RAW_DATA.split("\n")]

# First Half
def first_half():
    for i in range(0, len(data) - 1):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i]*data[j]


def second_half():
    for i in range(0, len(data) - 2):
        for j in range(i+1, len(data) - 1):
            for k in range(j+1, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i]*data[j]*data[k]

print(first_half())
print(second_half())