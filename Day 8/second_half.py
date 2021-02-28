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
    changed_line = 0
    INSTRUCTION = 0
    AMOUNT = 1
    while changed_line < len(program):
        # We're ensured that program will end by changing one
        # instruction so we won't check we exceed the program's length
        while program[changed_line][INSTRUCTION] == 'acc':
            # Skip acc
            changed_line += 1
        print(f"Changing Line {changed_line}") 
        # Get a copy of our program
        altered_program = program.copy()
        # Flip one instruction at the current try index
        altered_program[changed_line] = ('nop', altered_program[changed_line][AMOUNT]) if altered_program[changed_line][INSTRUCTION] == 'jmp' else ('jmp', altered_program[changed_line][AMOUNT]) 
        # Run the program and check whether it finishes or repeats a line
        current_line = 0
        accumulator = 0
        executed_lines = set()
        while True:
            print("Running Program")
            if current_line == len(altered_program):
                print(f"Found solution by changing line {changed_line}!")
                # We've executed the last line. Program finished execution!
                return accumulator
            if current_line in executed_lines:
                # We have repeated a line -> Infinite Loop
                # Increase our changed_line counter and retry.
                changed_line += 1
                print(f"Infinite Loop at line {current_line}!")
                break    
            instruction = altered_program[current_line][INSTRUCTION]
            amount = altered_program[current_line][AMOUNT]
            executed_lines.add(current_line)
            if instruction == 'nop': 
                current_line += 1
            if instruction == 'acc':
                accumulator += amount
                current_line += 1
            if instruction == 'jmp':
                current_line += amount
    return 'No solution for this program found'

print(solve(program))