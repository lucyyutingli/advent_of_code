from functools import reduce

file = open("day13_input.txt", "r")
notes = file.read().split()

earliest = int(notes[0])
bus_temp = notes[1].split(",")
bus_ids = []
for i in bus_temp:
    if i != "x":
        bus_ids.append(int(i))
    else:
        bus_ids.append(i)


def waiting_id(start_time, array):
    current = start_time
    while(True):
        for i in array:
            if current%i == 0:
                return ((current-start_time)*i)
        current += 1

# print(waiting_id(earliest, bus_ids))

""" These Chinese remainder theorem functions are not my own. You can find them at: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6"""
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def find_time(array):
    n = []
    a = []
    for i,j in enumerate(array):
        if j != "x":
            n.append(j)
            a.append(j-i)
    print(n)
    print(a)
    print(chinese_remainder(n, a))

find_time(bus_ids)
# print(chinese_remainder([3,7,10], [2,4,5]))
