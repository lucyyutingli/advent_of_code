from collections import defaultdict

open_file = open("day10_input.txt")
adapters = open_file.read().split()
int_adapters = [0]

for i in adapters:
    j = int(i)
    int_adapters.append(j)

int_adapters.sort()

def count_jumps(int_adapters):
    single_jump = 0
    three_jump = 0

    sorted_adapters = sorted(int_adapters)
    print(sorted_adapters)
    current = sorted_adapters[0]
    for i in sorted_adapters[1:]:
        if i - current == 1:
            single_jump += 1
        elif i - current == 3:
            three_jump += 1
        current = i

    print(single_jump, three_jump)
    return (single_jump+1) * (three_jump+1)


def recur_permutations(array):
    possible_ways = defaultdict(int)
    possible_ways[0] = 1
    for i in array[1:]:
        possible_ways[i] = possible_ways[i-1]+possible_ways[i-2]+possible_ways[i-3]

    return possible_ways

print(recur_permutations(int_adapters))
