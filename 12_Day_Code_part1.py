# imports

# --- functions here --- # 
def rot_dir(current_dir, rotation):

    directions = ['N', 'E', 'S', 'W']
    change_dir = int(rotation / 90)
    current_index = directions.index(current_dir)
    new_index = (current_index + change_dir) % (len(directions))
    new_dir = directions[new_index]

    return new_dir

# --- main here --- # 

#with open("12_Day_Test.txt", "r") as file:
with open("12_Day_Input.txt", "r") as file:
    data = file.read()

direction_list = data.split("\n")

len_east_west = 0
len_north_south = 0
current_dir = 'E'


for row in direction_list:
    if row[0] == 'F':
        row = current_dir + row[1:]

    if row[0] == 'N':
        len_north_south = len_north_south + int(row[1:])
    elif row[0] == 'S':
        len_north_south = len_north_south - int(row[1:])
    elif row[0] == 'E':
        len_east_west = len_east_west + int(row[1:])
    elif row[0] == 'W':
        len_east_west = len_east_west - int(row[1:])
    elif row[0] == 'R':
        current_dir = rot_dir(current_dir, int(row[1:]))
    else: # row[0] == 'L':
        current_dir = rot_dir(current_dir, int(row[1:])*-1)

print(len_north_south)
print(len_east_west)

print(abs(len_north_south) + abs(len_east_west))

