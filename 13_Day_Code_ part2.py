# imports

# --- functions here --- # 

def upper_while(ts):
    i = int((ts - 6) / 31)
    while ((59)*i - 2) % (31) != 0:
        i = i + 1
    ts = 31*i +6
    return ts

# --- main here --- # 

with open("13_Day_Test.txt", "r") as file:
#with open("13_Day_Input.txt", "r") as file:
    data = file.read()

my_data = data.split("\n")
timestamp = int(my_data[0])
my_buses = my_data[1].split(',')

bus_num = []
for i in range(len(my_buses)):
    if my_buses[i].isdigit():
        bus_num.append([int(my_buses[i]), i])

print(timestamp)
print(bus_num)

ts = 1000
"""
while ts % 7 != 0:
   # nested whiles here down to the primary jump loop  
    while ts + 7 % (19) != 0:
        i = upper_while(i)
        print(i)
        #i = i + 1
"""
while ts % 7 != 0:
   # nested whiles here down to the primary jump loop  
    while ts + 1 % (13) != 0:
            while ts + 7 % (19) != 0:
                ts = upper_while((ts-6)/31)
                print(i)
            ts = ts + 1
            print(ts)
    ts = ts + 1        
    print(ts)
    
    



print(i)
time_step = 31*i + 6
print(time_step)
