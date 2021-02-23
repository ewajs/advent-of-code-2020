from raw_data import RAW_DATA

def first_half():
    return sum([ 
        int(min) <= password.count(letter) <= int(max)
        for min, max, letter, password in [
        (min, *maxletter.split(" "), password) 
            for min, maxletter, password in [
                (*rule.split("-"), password) 
                for rule, password in [
                    line.split(":") for line in RAW_DATA.strip().split("\n")
                    ]
                ]
            ]
        ])

def second_half():
    return  sum([ 
        bool(password[int(i)-1] == letter) ^ bool(password[int(j)-1] == letter)
        for i, j, letter, password in [
        (i, *jletter.split(" "), password) 
            for i, jletter, password in [
                (*rule.split("-"), password.strip()) 
                for rule, password in [
                    line.split(":") for line in RAW_DATA.strip().split("\n")
                    ]
                ]
            ]
        ])


print(first_half())
print(second_half())