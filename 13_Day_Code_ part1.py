# imports

# --- functions here --- # 



# --- main here --- # 

#with open("13_Day_Test.txt", "r") as file:
with open("13_Day_Input.txt", "r") as file:
    data = file.read()

my_data = data.split("\n")
timestamp = int(my_data[0])
my_buses = my_data[1].split(',')

bus_num = []
for bus in my_buses:
    if bus.isdigit():
        bus_num.append(int(bus))

print(timestamp)
print(bus_num)

next_bus = []

for bus in bus_num:
    min_till_next = bus - ((timestamp + bus) % bus)
    next_bus.append(min_till_next)

my_min = min(next_bus)
my_index = next_bus.index(my_min)
my_bus = bus_num[my_index]


print(my_min)
print(my_bus)
print(my_bus * my_min)
