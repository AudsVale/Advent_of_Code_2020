# imports here

# --- functions here --- #
def jump(my_list):
    calc_jump = []
    for i in range(0,(len(my_list)-1)):
        calc_jump.append(my_list[i+1]-my_list[i])
    calc_jump.append(3)
    return calc_jump

def count_jumps(my_list, num_skips):
    count = 0
    for skip in my_list:
        if skip == num_skips:
            count = count + 1
    return count

def count_singles(my_list):
    count_ones = []
    count = 0
    for jump in my_list:
        if jump == 1:
            count = count + 1
        if jump == 3: 
            count_ones.append(count)
            count = 0
    return count_ones

def transform_singels(my_list):
    transformed_list = []
    for count in my_list:
        if count == 0 or count == 1: # how many compinations are possible for the count of ones 
            transformed_list.append(1) # ex: 3 > 111, 021, 102, 003 -> 4
        elif count == 2:
            transformed_list.append(2)
        elif count == 3:
            transformed_list.append(4)
        elif count == 4:
            transformed_list.append(7)
        elif count == 5:
            transformed_list.append(10)
        else:
            transformed_list.append(0) # if multi returns a null, then we have a group of ones larger than 5 
    print(transformed_list)
    return transformed_list

def multi_list(my_list): # muliplying the number of combies for each segment of ones generates the total number of combies
    multi = 1
    for num in my_list:
        multi = multi * num
    return multi

# --- main here --- #

my_adapters = []
f = open("./10_Day_Test.txt", "r")
#f = open("./10_Day_Input.txt", "r")

for line in f:
    my_adapters.append(int(line.rstrip()))

#print(my_adapters)

adapters_sorted = sorted(my_adapters)
adapters_sorted_null = [0]
for adapters in adapters_sorted:
    adapters_sorted_null.append(adapters)

#print(adapters_sorted_null)

jumps = jump(adapters_sorted_null)
print(jumps)

counted_singels = count_singles(jumps)
transformed_combis = transform_singels(counted_singels)
combies = multi_list(transformed_combis)

print(combies)