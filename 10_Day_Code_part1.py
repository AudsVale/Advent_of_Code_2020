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

# --- main here --- #

my_adapters = []
#f = open("./10_Day_Test.txt", "r")
f = open("./10_Day_Input.txt", "r")

for line in f:
    my_adapters.append(int(line.rstrip()))

#print(my_adapters)

adapters_sorted = sorted(my_adapters)
adapters_sorted_null = [0]
for adapters in adapters_sorted:
    adapters_sorted_null.append(adapters)

#print(adapters_sorted_null)

jumps = jump(adapters_sorted_null)
#print(jumps)

count_single_jumps = count_jumps(jumps, 1)
#print(count_single_jumps)
count_triple_jumps = count_jumps(jumps, 3)
#print(count_triple_jumps)

print(count_single_jumps*count_triple_jumps)