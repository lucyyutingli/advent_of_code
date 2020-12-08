new_file = open("day8_input.txt")
instructions = new_file.readlines()
in_sorted = []

for i in instructions:
    j = i.split()
    in_sorted.append([j[0], j[1]])


def sum_accumulator(instructions):
    acc = 0
    current = 0
    finished = False

    visited = []
    while(True):
        if current in visited:
            break
        else:
            visited.append(current)
            
            if instructions[current][0] == 'nop':
                current += 1
            elif instructions[current][0] == 'acc':
                acc += int(instructions[current][1])
                current += 1
            elif instructions[current][0] == 'jmp':
                current += int(instructions[current][1])
            if current == len(in_sorted):
                finished = True
                break

    return acc, finished




def switch_up(index, array):
    if array[index][0] == 'nop':
        array[index][0] = 'jmp'
    elif array[index][0] == 'jmp':
        array[index][0] = 'nop'

    return array

def part_2(instructions):
    pos = 0
    stop = False
    while(stop != True):
        print(instructions[pos])
        instructions = switch_up(pos, instructions)
        score, finished = sum_accumulator(instructions)
        if finished == False:
            instructions = switch_up(pos, instructions)
            pos += 1
        else:
            break
    return score



print(part_2(in_sorted))


    

# print(sum_accumulator(in_sorted))
