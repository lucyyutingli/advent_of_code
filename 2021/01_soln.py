


def increase_count(list_nums):
    
    
    increases= 0
    
    for i in range(1, len(lines)):
        print(lines[i], lines[i-1])
        
        if lines[i] > lines[i-1]:
            print("increased")
            increases += 1
    
    print(increases)
    

def sliding_window(list_nums):
    
    last_num = list_nums[0] + list_nums[1] + list_nums[2]
    curr_sum = 0
    increased = 0
    
    for i in range(1, len(list_nums)):
        if i >= len(list_nums)-2:
            break
        
        curr_sum = list_nums[i] + list_nums[i+1] + list_nums[i+2]
        
        if curr_sum > last_num:
            increased += 1
            
        last_num = curr_sum

    print(increased)
    
if __name__ == '__main__':
    
    depth_file = open("01_input.txt", "r")
    lines = depth_file.readlines()
    lines = [int(i) for i in lines]
    
    # increase_count("lines")
    sliding_window(lines)
                                                                
    