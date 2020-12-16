#totally didn't abandon this one and just copy Max from step 2 onward.
#origally did part 1 with some recursive method shown below

def findLoop(data, part1=False):
    acc, pc = 0, 0
    visited = set()
    while True:
        if pc == len(data):
            return acc
        elif pc in visited:
            return acc if part1 else None
        cmd, arg = data[pc].split(' ')
        if cmd == 'acc':
            acc += int(arg)
        elif cmd == 'jmp':
            pc += int(arg)
            continue
        visited.add(pc)
        pc += 1

def fixLoop(data):
    for i in range(len(data)):
        dataCopy = data[:]
        instr, value = dataCopy[i].split(' ')
        if instr == "jmp":
            dataCopy[i] = f'nop {value}'
        elif instr == "nop":
            dataCopy[i] = f'jmp {value}'
        else:
            continue
        acc = findLoop(dataCopy)
        if acc is not None:
            return acc

with open('input.txt', 'rt') as f:
        data = [line.strip() for line in f.readlines()]

result1 = findLoop(data, True)
result2 = fixLoop(data)
print(result1)
print(result2)

# My old code, not the farthest I got, but at this point part 1 works

#oldInstr = {}
#accumulator = 0

#def parseInstr(currentLine):
#    instr, number = currentLine.split(" ")
#    value = int(number)
#    return(instr, value)
#
#def handleInstr(instr, value, current, accumulator):
#     nextLine = current + 1
#     if instr == "acc":
#         accumulator += value
#         nextLine = current + 1
#     if instr == "jmp":
#         nextLine = current + value
#     if instr == "nop":
#         nextLine = current + 1
#     return(nextLine, accumulator)

# def findLoop(current, data, accumulator):
#     if(oldInstr.get(current) != None):
#         return(accumulator)
#     oldInstr.setdefault(current, 1)
#     currentLine = data[current]
#     instr, value = parseInstr(currentLine)
#     nextLine, accumulator = handleInstr(instr, value, current, accumulator)
#     return(findLoop(nextLine, data, accumulator))

# with open('input.txt', 'rt') as f:
#         data = [line.strip() for line in f.readlines()]

# accumulator = findLoop(0, data, accumulator)
# print(accumulator)