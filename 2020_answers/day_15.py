from collections import defaultdict

num_order = [1,0,16,5,17,4]

def taking_turns(array):
    turn_list = [0]*30000000
    turn_dict = defaultdict(list)
    for i,j in enumerate(array):
        turn_list[i] = j
        turn_dict[str(j)].append(i)
    
    for i,j in enumerate(turn_list):
        if i < len(num_order):
            continue
        else:
            if len(turn_dict[str(turn_list[i-1])]) == 1:
                turn_list[i] = 0
                turn_dict["0"].append(i)
                
            else:
                turn_list[i] = turn_dict[str(turn_list[i-1])][-1] - turn_dict[str(turn_list[i-1])][-2]
                turn_dict[str(turn_list[i])].append(i)
    
    print(turn_list[29999999])
    
taking_turns(num_order)
