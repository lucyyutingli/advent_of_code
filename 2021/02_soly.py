
def commands(lines):
    
    x = 0
    y = 0
    
    for i in lines:
        direction = i.split(" ")[0]
        value = int(i.split(" ")[1])
        
        if direction == "forward":
            x += value
        elif direction == "down":
            y += value
        elif direction == "up":
            y -= value

    print(x * y)

def commands(lines):
    
    x = 0
    y = 0
    aim = 0
    
    for i in lines:
        direction = i.split(" ")[0]
        value = int(i.split(" ")[1])
        
        if direction == "forward":
            x += value
            y += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

    print(x * y)


if __name__ == '__main__':
    
    file = open("02_input.txt", "r")
    lines = file.readlines()
    
    commands(lines)
    