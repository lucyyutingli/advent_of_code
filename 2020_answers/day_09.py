new_file = open("day9_input.txt")
numbers = new_file.read().split()
new_numbers = []


for i in numbers:
    j = int(i)
    new_numbers.append(j)


def find_not_sum(arr):
    first_index = 0
    last_index = 25
    for i in arr[25:]:
        temp_array = []
        for j in arr[first_index:last_index]:
            for k in arr[first_index:last_index]:
                temp_array.append(j+k)
        new_set = set(temp_array)
        if i not in new_set:
            return i

        first_index += 1
        last_index += 1


def find_weakness(num, array):
    for i in range(len(array)):
        for j in range (i, len(array)):
            out = sum(array[i:j])
            if out == num:
                return min(array[i:j]) + max(array[i:j])

    
print(find_not_sum(new_numbers))
out = find_not_sum(new_numbers)
print(find_weakness(out, new_numbers))
            

