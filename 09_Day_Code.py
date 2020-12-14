# imports here

# --- functions here --- #
def find_error(my_nim_list, recall_number):
    #start = recall_number
    for i in range(recall_number, len(my_nim_list)):
        my_test = False
        for j in range(i-recall_number,i-2):
            for k in range(j+1,i-1):
                if my_nim_list[j] + my_nim_list[k] == my_nim_list[i]:
                    my_test = True
                    break
                else:
                    continue
                break
            else:
                continue
            break
        if my_test == False:
            return i
    
        
        
# --- main here --- #

my_code = []
f = open("./09_Day_Test.txt", "r")
#f = open("./09_Day_Input.txt", "r")

for line in f:
    my_code.append(int(line.rstrip()))

#print(my_code)

preamble = 25

index_error = find_error(my_code, preamble)
print(my_code[index_error])

