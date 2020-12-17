import re
from collections import defaultdict

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
        memory_id = re.search(r'\[(.+?)\]', i).group(1)
        memory_input = int(i.split(" ")[2])
        memory_num.append((memory_id, memory_input))
        
    return mask, memory_num


def masked_memories(mask, array):
    mem = defaultdict()
    for i in array:
        new_bit = ""
        original_bit ="{0:036b}".format(i[1])
        for j,k in enumerate(mask):
            if k == "X":
                new_bit += original_bit[j]
            elif k == "1":
                new_bit += "1"
            elif k == "0":
                new_bit += "0"
        mem[i[0]] = int(new_bit,2)
    return sum(mem.values())

def complete_sum(array):
    total = 0
    for i in array:
        mask, memory_list = clean_groups(i)
        total += masked_memories(mask, memory_list)
    print(total)
    
complete_sum(mask_groups)
    

