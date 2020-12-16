from collections import deque

new_file = open("day12_input.txt","r")
commands = new_file.read().split()

def find_place(array):
    current_direction = "E"
    current_index = 2
    direction_array = ["W", "N", "E", "S"]
    directions_dict = {"W": 0, "N": 0, "E": 0, "S": 0}
    
    for i in array:
        direction = i[0]
        number = int(i[1:])
        if direction == "F":
            directions_dict[current_direction] += number
        elif direction == "R":
            turn_num = ((number//90)%4 + current_index) % 4
            current_direction = direction_array[turn_num]
            current_index = direction_array.index(current_direction)   
        elif direction == "L":
            turn_num = (-(number//90)%4 + current_index) % 4
            current_direction = direction_array[turn_num]
            current_index = direction_array.index(current_direction)
            
        else:
            directions_dict[direction] += number
    print(abs(directions_dict["N"] - directions_dict["S"]) + abs(directions_dict["E"] - directions_dict["W"]))
    
# find_place(commands)
        
        
def waypoint(array):
    #(n_s, e_w)
    waypoint_dict = {"W": 0, "N": 1, "E": 10, "S": 0}
    ship_dict = {"W": 0, "N": 0, "E": 0, "S": 0}
    
    for i in array:
        num = int(i[1:])
        if i[0] == "F":
            ship_dict["W"] += (waypoint_dict["W"]*num)
            ship_dict["N"] += (waypoint_dict["N"]*num)
            ship_dict["E"] += (waypoint_dict["E"]*num)
            ship_dict["S"] += (waypoint_dict["S"]*num)
        elif i[0] == "R":
            turn_num = (num//90)%4
            current_waypoint = deque([waypoint_dict["W"], waypoint_dict["N"], waypoint_dict["E"], waypoint_dict["S"]])
            current_waypoint.rotate(turn_num)
            waypoint_dict.update({"W": current_waypoint[0], "N": current_waypoint[1], "E": current_waypoint[2], "S": current_waypoint[3]})
        elif i[0] == "L":
            turn_num = (num//90)%4
            current_waypoint = deque([waypoint_dict["W"], waypoint_dict["N"], waypoint_dict["E"], waypoint_dict["S"]])
            current_waypoint.rotate(-turn_num)
            waypoint_dict.update({"W": current_waypoint[0], "N": current_waypoint[1], "E": current_waypoint[2], "S": current_waypoint[3]})
        else:
            waypoint_dict[i[0]] += num
    print(abs(ship_dict["N"] - ship_dict["S"]) + abs(ship_dict["E"] - ship_dict["W"]))

waypoint(commands)
