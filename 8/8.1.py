def execute_instruction(instruction, ip, acc):
    command, value = instruction.split()
    value = int(value)
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
            return acc
        visited.append(ip)
        ip, acc = execute_instruction(program[ip], ip, acc)


program = open('8/input.txt').read().splitlines()
print(find_loop(program))