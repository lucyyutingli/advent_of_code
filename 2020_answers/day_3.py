def num_of_trees(file):
    tree_file = open(file, "r")
    Lines = tree_file.readlines()
    
    first_check_pos = 1
    first_tree_num = 0
    for i in Lines[1:]:
        if i[first_check_pos % 31] == "#":
            first_tree_num += 1
        first_check_pos += 1
    
    position = 3
    tree_num = 0
    for i in Lines[1:]:
        if i[position % 31] == "#":
            tree_num += 1
        position += 3
    
    third_tree_pos = 5
    third_tree_num = 0
    for i in Lines[1:]:
        if i[third_tree_pos % 31] == "#":
            third_tree_num += 1
        third_tree_pos += 5
        
    fourth_tree_pos = 7
    fourth_tree_num = 0
    for i in Lines[1:]:
        if i[fourth_tree_pos % 31] == "#":
            fourth_tree_num += 1
        fourth_tree_pos += 7
        
    fifth_tree_pos = 1
    fifth_tree_num = 0
    for i,j in enumerate(Lines[2:]):
        if i % 2 != 0:
            continue
        elif j[fifth_tree_pos % 31] == "#":
            fifth_tree_num += 1
        fifth_tree_pos += 1
    
    print(fifth_tree_num, fourth_tree_num, third_tree_num, tree_num, first_tree_num)
    return fifth_tree_num* fourth_tree_num* third_tree_num* tree_num* first_tree_num

result = num_of_trees("tree_input.txt")

print(result)
