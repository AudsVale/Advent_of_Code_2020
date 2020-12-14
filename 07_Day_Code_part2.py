"""--- Part Two ---

It's getting pretty expensive to fly these days - not because of ticket prices, 
but because of the ridiculous number of bags you need to buy!
Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags 
(and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!
Of course, the actual rules have a small chance of going several levels deeper than this example; 
be sure to count all of the bags, even if the nesting becomes topologically impractical!
Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.
How many individual bags are required inside your single shiny gold bag?
"""

# --- FUNCTIONS HERE --- #
def rule_to_dict(rule):
    line = {}
    rule = rule.split(' bag')
    rule_key = rule[0]
    value_list = []
    for i in range(1,len(rule)):
        for j in range(len(rule[i])): 
            if rule[i][j].isdigit():
                value_list.append(int(rule[i][j]))
                value_list.append(rule[i][j+2:])
    return rule_key, value_list
    
def list_inner_bags(my_dict, outer_bag, loop):
    inner_list = outer_bag
    for i in outer_bag[loop]:
        for outer, inner in my_dict.items():
            if outer == i:
                inner_list.append(inner)
    return inner_list

def calc_inner_bags(my_dict, outer_bag):
    my_bag = outer_bag.copy()
    for i in range(len(my_bag)):
        for outer, inner in my_dict.items():
            if outer == my_bag[i]:
                my_bag[i] = inner
    return my_bag


# --- MAIN HERE --- #
#with open("07_Day_Test.txt", "r") as file:
with open("07_Day_Input.txt", "r") as file:
    data = file.read()

rule_list = data.split("\n")
#print(rule_list)

rule_dict = {}
for i in range(len(rule_list)):
    key, values = rule_to_dict(rule_list[i])
    rule_dict[key] = values

print(rule_dict)

#bags_in_bags = [[1, 'shiny gold']]

""" i = 0
while len(bags_in_bags[len(bags_in_bags) - 1]) != 0:
    bags_in_bags = list_inner_bags(rule_dict, bags_in_bags, i)
    i = i + 1
    print(bags_in_bags) """

start_bag = [1, 'shiny gold']
round_01 = calc_inner_bags(rule_dict, start_bag)

mulitpliers = []
mulitpliers.append(round_01[0])
round_02 = calc_inner_bags(rule_dict, round_01[1])

print(round_02)

multi = []
calc_me = []
for i in range(len(round_02)):
    if i%2 == 0:
        multi.append(round_02[i])
    else:
        calc_me.append(round_02[i])
    
mulitpliers.append(multi)
#print(calc_me)
#print(mulitpliers)







    