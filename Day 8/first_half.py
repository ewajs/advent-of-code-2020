from raw_data import RAW_DATA

test_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".strip()



program = [(instruction, int(amount))for instruction, amount in [
    line.split() for line in RAW_DATA.split("\n")
    ]
]

def solve(program):
    current_line = 0
    INSTRUCTION = 0
    AMOUNT = 1
    executed_lines = set()
    accumulator = 0
    while True:
        if current_line in executed_lines:
            return accumulator
        instruction = program[current_line][INSTRUCTION]
        amount = program[current_line][AMOUNT]
        executed_lines.add(current_line)
        if instruction == 'nop': 
            current_line += 1
        if instruction == 'acc':
            accumulator += amount
            current_line += 1
        if instruction == 'jmp':
            current_line += amount

print(solve(program))