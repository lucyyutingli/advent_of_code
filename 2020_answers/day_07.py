from collections import defaultdict

new_file = open("day7_input.txt","r")
all_bag_rules = new_file.readlines()
    

    
def search_for_bag(bag, list_bag):
    full_bag_list = []
    
    counter = 0
    for i in list_bag:
        if bag in i:
            counter += 1
            full_bag_list.append(i)
            
    shortened_bag_list = []
    for i in full_bag_list:
        j = i.split(" ")
        bag_to_add = j[0] + " " + j[1]
        if bag_to_add == bag:
            continue
        else:
            shortened_bag_list.append(bag_to_add)
          
    return(counter, shortened_bag_list)

counter = 0
first = search_for_bag("shiny gold", all_bag_rules)
first_layer = first[1]

seen = []
while(len(first_layer) != 0):
    # print(first_layer)
    k = first_layer[0]
    first_layer.pop(0)
    if k not in seen:
        first_layer += search_for_bag(k, all_bag_rules)[1]
        seen.append(k)
        counter += 1
        # print(counter)

    
starting = ""
for i in all_bag_rules:
    if "shiny gold bags contain" in i:
        starting += i

bag_to_contain = defaultdict(list)        
for i in all_bag_rules:
    if i.endswith("no other bags.\n"):
        continue
    parent, children = i.split("contain")
    parent = parent.replace("bags", "").strip()
    for child in children.split(","):
        child = child.split()
        print(child)
        n = int(child[0])
        child = " ".join(child[1:-1])
        bag_to_contain[parent].append((child,n))
        
total = 0
queue = [("shiny gold", 1)]
while queue:
    bag_color,n = queue.pop()
    total += n
    for (bag_color_2, n_2) in bag_to_contain[bag_color]:
        queue.append((bag_color_2, n_2 * n))
        
print({total-1})
