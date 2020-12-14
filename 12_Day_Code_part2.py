# imports

# --- functions here --- # 
def rot_dir(waypoint_east_west, waypoint_north_south, rotation):

    change_dir = int(rotation / 90) % 4

    if change_dir == 1:
        waypoint_east_west_new = waypoint_north_south
        waypoint_north_south_new = waypoint_east_west * -1
    elif change_dir == 2:
        waypoint_east_west_new = waypoint_east_west * -1
        waypoint_north_south_new = waypoint_north_south * -1
    elif change_dir == 3:
        waypoint_east_west_new = waypoint_north_south * -1
        waypoint_north_south_new = waypoint_east_west
    else: # 0 or 360
        waypoint_east_west_new = waypoint_east_west 
        waypoint_north_south_new = waypoint_north_south 

    return waypoint_east_west_new, waypoint_north_south_new

# --- main here --- # 

#with open("12_Day_Test.txt", "r") as file:
with open("12_Day_Input.txt", "r") as file:
    data = file.read()

direction_list = data.split("\n")

ship_east_west = 0
ship_north_south = 0

waypoint_east_west = 10
waypoint_north_south = 1


for row in direction_list:
    if row[0] == 'F':
        ship_east_west = ship_east_west + (waypoint_east_west * int(row[1:]))
        ship_north_south = ship_north_south + (waypoint_north_south * int(row[1:]))

    elif row[0] == 'N':
        waypoint_north_south = waypoint_north_south + int(row[1:])
    elif row[0] == 'S':
        waypoint_north_south = waypoint_north_south - int(row[1:])
    elif row[0] == 'E':
        waypoint_east_west = waypoint_east_west + int(row[1:])
    elif row[0] == 'W':
        waypoint_east_west = waypoint_east_west - int(row[1:])
    elif row[0] == 'R':
        waypoint_east_west, waypoint_north_south = rot_dir(waypoint_east_west, waypoint_north_south, int(row[1:]))
    else: # row[0] == 'L':
        waypoint_east_west, waypoint_north_south = rot_dir(waypoint_east_west, waypoint_north_south, int(row[1:])*-1)

print(ship_east_west)
print(ship_north_south)

print(abs(ship_east_west) + abs(ship_north_south))

