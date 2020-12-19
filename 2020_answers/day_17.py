"""This file was mostly not my own. I really struggled with this days and had to get some inspiration from a nice person on Reddit. 
   Find their solution here: https://pastebin.com/GBqvkXAv"""
   
   from collections import defaultdict
from numpy import copy
import itertools

file = open("day17_input.txt", "r")
first = file.read().split('\n')

coord_dict = {}

y = 0
z = 0
w = 0

for i in first:
    for x,j in enumerate(i):
        coord_dict[(x,y,z,w)] = j
    y += 1

def neighbor_list(coord: tuple):
    tx = coord[0]
    ty = coord[1]
    tz = coord[2]
    tw = coord[3]
    coord_list = []
    for nx in range(tx -1, tx +2):
        for ny in range(ty-1, ty+2):
            for nz in range(tz-1, tz+2):
                for nw in range(tw-1, tw+2):
                    coord_list.append((nx,ny,nz,nw))
    coord_list.remove((tx, ty, tz, tw))
    return coord_list
    
def update_cubes(coord_dict: dict):
    neighbor_count = {}
    for coord in coord_dict:
        if coord_dict[coord] == "#":
            neigh_list = neighbor_list(coord)
            for neighbor in neigh_list:
                try:
                    neighbor_count[neighbor] += 1
                except KeyError:
                    neighbor_count[neighbor] = 1
                    
                    
    new_map = {}
    active_count = 0
    
    for coord in neighbor_count:
        try:
            current_state = coord_dict[coord]
        except KeyError:
            current_state = "."
            
        if current_state == "#" and not (2 <= neighbor_count[coord] <= 3):
            new_map[coord] = "."
        elif current_state == "." and neighbor_count[coord] == 3:
            new_map[coord] = "#"
        else:
            new_map[coord] = current_state
            
        if new_map[coord] == "#":
            active_count += 1
            
    return new_map, active_count


def final(coord_dict):
    for i in range(6):
        coord_dict, counter = update_cubes(coord_dict)
    
    print(counter)
    
final(coord_dict)
