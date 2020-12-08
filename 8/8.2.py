def parse_instruction(instruction):
    command, value = instruction.split()
    value = int(value)
    return command, value

def execute_instruction(command, value, ip, acc):
    if command == "nop":
        ip += 1
    elif command == "acc":
        acc += value
        ip += 1
    elif command == "jmp":
        ip += value
    else:
        pass
    return ip, acc

def find_loop(program):
    visited = []
    acc = 0
    ip = 0
    while True:
        if ip in visited:
            return acc, True
        if ip == len(program):
            return acc, False
        
        visited.append(ip)
        ip, acc = execute_instruction(*parse_instruction(program[ip]), ip, acc)

def substitute_command(program, commands_to_replace, replace_with):
    for index in commands_to_replace:
        _, value = parse_instruction(program[index])
        new_command = f"{replace_with} {value}"
        if index == 0:
            acc, loop = find_loop([new_command] + program[index+1:])
        else: 
            acc, loop = find_loop(program[:index] + [new_command] + program[index+1:])
        if not loop:
            print(acc)
            exit() 

program = open('8/input.txt').read().splitlines()
jumps = [i for i, x in enumerate(program) if "jmp" in x]
nops = [i for i, x in enumerate(program) if "nop" in x]
substitute_command(program, jumps, "nop")
substitute_command(program, nops, "jmp")
     