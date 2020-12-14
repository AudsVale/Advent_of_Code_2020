# imports here
import copy

# --- FUNCTIONS HERE --- #
def correct_me(rule_list, loop):
    my_rule_list = copy.deepcopy(rule_list)
    i = 0
    while i <= loop:
        for j in range(len(my_rule_list)):
            if my_rule_list[j][0] == 'nop':
                if i == loop:
                    my_rule_list[j][0] = 'jmp'
                i = i + 1
            elif my_rule_list[j][0] == 'jmp':
                if i == loop:
                    my_rule_list[j][0] = 'nop'
                i = i + 1
            else: # acc
                continue
    return my_rule_list


def check_loop_acc(my_list):
    commands_ran = []
    acc = 0
    i = 0       
    while i not in commands_ran and i < len(my_list):
        if my_list[i][0] == 'nop':
            commands_ran.append(i)
            i = i + 1 
            continue
        elif my_list[i][0] == 'acc':
            commands_ran.append(i)
            operator = my_list[i][1][0]
            number = int(my_list[i][1][1:])
            if operator == '+':
                acc = acc + number
            else: # '-'
                acc = acc - number
            i = i + 1 
            continue
        else: # jmp
            commands_ran.append(i)
            operator = my_list[i][1][0]
            number = int(my_list[i][1][1:])
            if operator == '+':
                i = i + number
            else: # '-'
                i = i - number
            continue
    check = True
    if i < len(my_list):
        check = False
    return check, acc

# --- MAIN HERE --- # 

#with open("08_Day_Test.txt", "r") as file:
with open("08_Day_Input.txt", "r") as file:
    data = file.read()

rule_list = data.split("\n")

for i in range(len(rule_list)):
   rule_list[i] = rule_list[i].split()

#print(rule_list)

check = False
loop = 0
while check == False:
    my_rule_list = correct_me(rule_list, loop)
    #print(loop)
    #print(my_rule_list)
    check, acc = check_loop_acc(my_rule_list)
    loop = loop + 1

print(acc)