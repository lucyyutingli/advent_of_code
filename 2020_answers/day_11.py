import numpy

file = open("day11_input.txt","r")
rows = file.read().split()

temp = []
new_rows = []
for i in rows:
    new_rows.append(list(i))


def check_around(array, row, col):
    counter = 0
    num_rows = len(array)
    num_col = len(array[0])
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
            row_i = row+i
            col_j = col+j
            if row_i in range(num_rows) and col_j in range(num_col):
                if i == 0 and j == 0: continue
                if array[row_i][col_j] == "#":
                    counter += 1
                    
    return counter

def check_eight(array, row, col):
    counter = 0
    num_rows = len(array)
    num_col = len(array[0])
    k = 1
    row_i = 0
    col_j = 0
    for i in [-1,0,1]:
        for j in [-1, 0, 1]:
            # k=1 --> +1, -1
            # k=2 --> +2, +2
            if i == 0 and j == 0:
                continue
            k=1
            row_i = row+i*k
            col_j = col+j*k
            while (row_i in range(num_rows) and col_j in range(num_col)):
                if row_i in range(num_rows) and col_j in range(num_col):
                    if array[row_i][col_j] == "L":
                        break
                    if array[row_i][col_j] == "#":
                        counter += 1
                        break
                k += 1
                row_i = row+i*k
                col_j = col+j*k
    return counter
                        
            

def check_all(array):
    new_array = [[0 for x in range(len(array[0]))] for y in range(len(array))]
    for i in range(len(array)):
        for j in range(len(array[i])):
            checker = check_eight(array, i, j)
            if array[i][j] == "L" and checker == 0:
                new_array[i][j] = "#"
            elif array[i][j] == "#" and checker >= 5:
                new_array[i][j] = "L"
            else:
                new_array[i][j] = array[i][j]
           
    return new_array


            
def complete(array):
    equal = False
    current = array
    counter = 0
    while(equal == False):
        changed_seats = check_all(current)
        if current == changed_seats:
            equal = True
            break
        else:
            current = changed_seats
    for i in current:
        for j in i:
            if j == "#":
                counter += 1
                
    return counter
    
print(complete(new_rows))

    

