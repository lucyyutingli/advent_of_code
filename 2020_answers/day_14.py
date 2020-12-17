import re
from collections import defaultdict
from itertools import product

file = open("day14_input.txt", "r")
full_input = file.read().split('\n')

mask_groups = []
temp_group = []
for i in full_input:
    if i.startswith("mask"):
        if temp_group != []:
            mask_groups.append(temp_group)
        temp_group = []
        temp_group.append(i)
    else:
        temp_group.append(i)
mask_groups.append(temp_group)
        
        
def clean_groups(array):   
    mask = array[0].split()[2]
    memory_num = []        
    for i in array[1:]:
        memory_id = int(re.search(r'\[(.+?)\]', i).group(1))
        memory_input = int(i.split(" ")[2])
        memory_num.append((memory_id, memory_input))
        
    return mask, memory_num

global mem
mem = defaultdict()
def masked_memories(mask, array):
    global mem
    for i in array:
        new_bit = ""
        original_mem ="{0:036b}".format(i[0])
        for j,k in enumerate(mask):
            if k == "X":
                new_bit += "X"
            elif k == "1":
                new_bit += "1"
            elif k == "0":
                new_bit +=  original_mem[j]
    
        x_count = new_bit.count("X")
        possible_combos = [p for p in product([0,1], repeat = x_count)]
        
        for l in possible_combos:
            copy_bit = new_bit
            for j in l:
                copy_bit = copy_bit.replace("X", str(j), 1)
            mem[int(copy_bit,2)] = i[1]
            
            
            
def complete_sum(array):
    total = 0
    for i in array:
        mask, memory_list = clean_groups(i)
        masked_memories(mask, memory_list)
    total = sum(mem.values())
    print(total)
    
complete_sum(mask_groups)
    

