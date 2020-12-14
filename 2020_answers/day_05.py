def seat_id(file):
    new_file = open(file, "r")
    seats = new_file.readlines()
    seat_ids = []
    
    for i in seats:
        i = i[:-1]
        # print(i)
        row = front_back(i[0:7])
        row = int(row,2)
        col = left_right(i[7:])
        col = int(col,2)
        seat_ids.append(row * 8 + col)
    

    seat_ids.sort()
    print(seat_ids)
    current = 0
    for i in seat_ids:
        if i - current == 2:
            return i-1
        else:
            current = i


def front_back(string):
    bit_string = ""
    for i in string:
        if i == "F":
            bit_string += "0"
        elif i == "B":
            bit_string += "1"
    return bit_string

def left_right(string):
    bit_string = ""
    for i in string:
        if i == "L":
            bit_string += "0"
        if i == "R":
            bit_string += "1"
    return bit_string


print(seat_id("day5_input.txt"))
