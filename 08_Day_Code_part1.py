# imports here

# --- FUNCTIONS HERE --- #


# --- MAIN HERE --- # 

#with open("08_Day_Test.txt", "r") as file:
with open("08_Day_Input.txt", "r") as file:
    data = file.read()

rule_list = data.split("\n")

for i in range(len(rule_list)):
   rule_list[i] = rule_list[i].split()

#print(rule_list)

commands_ran = []
acc = 0
i = 0
while i not in commands_ran:
    if rule_list[i][0] == 'nop':
        commands_ran.append(i)
        i = i + 1 
        continue
    elif rule_list[i][0] == 'acc':
        commands_ran.append(i)
        operator = rule_list[i][1][0]
        number = int(rule_list[i][1][1:])
        if operator == '+':
            acc = acc + number
        else: # '-'
            acc = acc - number
        i = i + 1 
        continue
    else: # jmp
        commands_ran.append(i)
        operator = rule_list[i][1][0]
        number = int(rule_list[i][1][1:])
        if operator == '+':
            i = i + number
        else: # '-'
            i = i - number
        continue

print(acc)
