file = open("day18_input.txt", "r")
lines = file.read().split("\n")

    


# An equation that takes care of left to right mathematics (no parenthases considered)
def bad_maths(equation: str):
    current_num = 0
    current_op = None
    things = equation.split(" ")
    if "+" not in things and "*" not in things:
        return int(equation)
    for i,j in enumerate(things):
        if i == 0:
            current_num = int(j)
            continue   
        if j != "+" and j != "*":
            if current_op == "+":
                current_num += int(j)
            elif current_op == "*":
                current_num *= int(j)
        elif j == "+" or j == "*":
            current_op = j  
                
    return current_num

# An equation for new precendence rules
def worse_maths(equation: str):
    while("+" in equation):
        things = equation.split(" ")
        for i,j in enumerate(things):
            if j == "+":
                sum_replace = int(things[i-1]) + int(things[i+1])
                equation = equation.replace((things[i-1] + " + " + things[i+1]), str(sum_replace))
                break
    return bad_maths(equation)
    
    
# An equatin that slowly replaces nested parenthases
def parenthases(equation: str):
    starting = 0
    for i in equation:
        if i == ")":
            starting = equation.index(i)
            
    new_string = ""     
    for i in equation[starting-1::-1]:
        if i == "(":
            old_string = ("(" + new_string[len(new_string)::-1] + ")")
            return equation.replace(old_string, str(worse_maths(new_string[len(new_string)::-1])))
        else:
            new_string += i
            

def finale(array):
    total = 0
    for i in array:
        current = None
        new_string = i
        while(")" in new_string):
            new_string = parenthases(new_string)
        total += worse_maths(new_string)
                
    print(total)
    
finale(lines)  
                    
