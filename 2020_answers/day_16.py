from collections import defaultdict
from collections import Counter
from numpy import copy

new_file = open("day16_input.txt","r")
lines = new_file.read().split('\n')


field_dict = defaultdict(list)
my_ticket = None
nearby_tickets = None

for i,j in enumerate(lines):
    current_string = j.split(": ")
    if len(current_string) > 1:
        ranges = current_string[1].split(" or ")
        for numbers in ranges:
            x = numbers.split("-")
            field_dict[current_string[0]].extend(list(range(int(x[0]), int(x[1])+1)))
    else:
        if j.startswith("your ticket"):
            my_ticket = lines[i+1]
        if j.startswith("nearby tickets"):
            nearby_tickets = lines[i+1:]
    
my_ticket = my_ticket.split(",") 
    
    
def error_rate(dictionary, nearby):
    total_error = 0
    all_possible = sum(dictionary.values(), [])
    for ticket in nearby:
        all_values = ticket.split(",")
        for num in all_values:
            if int(num) not in all_possible:
                nearby.remove(ticket)
                break
    print(total_error)
    
def determine_fields(dictionary, nearby):
    len_fields = len(nearby[0].split(","))
    
    all_possible = sum(dictionary.values(), [])
    nearby_copy = nearby.copy()
    for ticket in nearby:
        all_values = ticket.split(",")
        for num in all_values:
            if int(num) not in all_possible:
                nearby_copy.remove(ticket)
                break
    
    index_groups = []
    for i in range(len_fields):
        current_group = []
        for j in nearby_copy:
            current_group.append(int(j.split(",")[i]))
        index_groups.append(current_group)
        
    candidate_groups = []
    for group in index_groups:
        temp_group = []
        for key in dictionary:
            if all(num in dictionary[key] for num in group):
                temp_group.append(key)
        candidate_groups.append(list(set(temp_group)))
        
        
    final_index = [0]*len_fields
    while(0 in final_index):
        copy_groups = candidate_groups.copy()
        for i,j in enumerate(copy_groups):
            if len(j) == 1:
                final_index[i] = j[0]
                for l,y in enumerate(candidate_groups):
                    candidate_groups[l] = [k for k in y if k != j[0]]
                    
    print(final_index)            
            


    
# error_rate(field_dict, nearby_tickets)
determine_fields(field_dict, nearby_tickets)          
