# imports here
import numpy as np
# --- functions here --- #
def add_floor(my_map):
    frame_floor = []
    frame_floor.append(list('.'*(len(my_map)+2)))
    i = 1
    for row in my_map:
        frame_floor.append(list('.' + row + '.'))
    frame_floor.append(list('.'*(len(my_map)+2)))
    return frame_floor

def check_in_direction(x, y, my_map, right, down): # down = -1 -> up and right = -1 -> left
    view_free = True
    i = y + down
    j = x + right
    while (i < len(my_map) and i >= 0) and (j < len(my_map[y]) and j >= 0):
            if my_map[i][j] == 'L':
                return view_free
            elif my_map[i][j] == '#':
                view_free = False
                return view_free
            else:
                i = i + down
                j = j + right
    return view_free


def count_in_view_filled_seats(y,x,my_map):
    dir_left_up    = check_in_direction(x, y, my_map, -1, -1)
    dir_0_up       = check_in_direction(x, y, my_map,  0, -1)
    dir_right_up   = check_in_direction(x, y, my_map,  1, -1)
    dir_right_0    = check_in_direction(x, y, my_map,  1,  0)
    dir_right_down = check_in_direction(x, y, my_map,  1,  1)
    dir_0_down     = check_in_direction(x, y, my_map,  0,  1)
    dir_left_down  = check_in_direction(x, y, my_map, -1,  1)
    dir_left_0     = check_in_direction(x, y, my_map, -1,  0)
    count = dir_left_up + dir_0_up + dir_right_up + dir_right_0 + dir_right_down + dir_0_down + dir_left_down + dir_left_0
    count = 8-count
    return count

def people_move(noone_moved, my_map):
    #generate an empty floorplan
    next_map = []
    count_map = []
    for row in my_map:
        next_map.append(list('.'*len(row)))
        count_map.append(list('.'*len(row)))
    #check if noone moves
    noone_moved = True
    #walk through map
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == '.': #do nothing
                continue
            elif my_map[i][j] == 'L':
                count = count_in_view_filled_seats(i,j,my_map)
                count_map[i][j] = count
                if count == 0:
                    next_map[i][j] = '#'
                    noone_moved = False 
                else:
                    next_map[i][j] = 'L'
            elif my_map[i][j] == '#':
                count = count_in_view_filled_seats(i,j,my_map)
                count_map[i][j] = count
                if count >= 5: # here 5 or more seats are filled from the 8 directions
                    next_map[i][j] = 'L'
                    noone_moved = False 
                else:
                    next_map[i][j] ='#'
    #print(np.matrix(count_map))
    #print('loop')
    return noone_moved, next_map


def count_filled_seats(my_map):
    count = 0
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == '#':
                count = count + 1
    return count


# --- main here --- #

my_map = []

#f = open("./11_Day_Test.txt", "r")
f = open("./11_Day_Input.txt", "r")

for line in f:
    my_map.append(line.rstrip())

#print(my_map)

my_map = add_floor(my_map)
#print(my_map)


noone_moved = False

while not noone_moved:
    noone_moved, my_map = people_move(noone_moved, my_map)
    #print(np.matrix(my_map))

count_people = count_filled_seats(my_map)

print(count_people)
