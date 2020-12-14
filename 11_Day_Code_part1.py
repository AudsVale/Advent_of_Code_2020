# imports here

# --- functions here --- #
def add_floor(my_map):
    frame_floor = []
    frame_floor.append(list('.'*(len(my_map)+2)))
    i = 1
    for row in my_map:
        frame_floor.append(list('.' + row + '.'))
    frame_floor.append(list('.'*(len(my_map)+2)))
    return frame_floor

#count filled seats
def count_surrunding_filled_seats(x,y,my_map):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue # dont count seat 
            elif my_map[i][j] == '#':
                count = count + 1
    return count

def people_move(noone_moved, my_map):
    #generate an empty floorplan
    next_map = []
    for row in my_map:
        next_map.append(list('.'*len(row)))
    #check if noone moves
    noone_moved = True
    #walk through map
    for i in range(len(my_map)):
        for j in range(len(my_map[i])):
            if my_map[i][j] == '.': #do nothing
                continue
            elif my_map[i][j] == 'L':
                count = count_surrunding_filled_seats(i,j,my_map)
                if count == 0:
                    next_map[i][j] = '#'
                    noone_moved = False 
                else:
                    next_map[i][j] = 'L'
            elif my_map[i][j] == '#':
                count = count_surrunding_filled_seats(i,j,my_map)
                if count >= 4:
                    next_map[i][j] = 'L'
                    noone_moved = False 
                else:
                    next_map[i][j] ='#'
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

#print(my_map)

count_people = count_filled_seats(my_map)

print(count_people)
