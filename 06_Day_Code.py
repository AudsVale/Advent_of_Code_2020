"""
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration 
forms are distributed to the passengers.
The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions 
for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.
However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. 
For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. 
(Duplicate answers to the same question don't count extra; each question counts at most once.)
Another group asks for your help, then another, and eventually you've collected answers from 
every group on the plane (your puzzle input). Each group's answers are separated by a blank line, 
and within each group, each person's answers are on a single line. For example:

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:
You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions 
to which everyone answered "yes"!

Using the same example as above:

This list represents answers from five groups:

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

"""
# --- FUNCTIONS HERE --- #

def individ_count(my_array):
    count_array = []
    for group in my_array:
        question_list = []
        for person in group: # now walk through people 
            for question in person:
                if question not in question_list:
                    question_list.append(question)
        #print(question_list)
        count_array.append(len(question_list))
    return count_array

def group_count(my_array):
    group_questions = []
    for group in my_array:
        all_answer = []
        question_list = {}
        lenght_group = len(group)
        for i in group[0]: # group[0] = first person in array, creates a key for the letter and a count of 1 occurance
            question_list[i] = 1
        for j in range(1, lenght_group): # now walk through people 
            for question in group[j]:
                #if question not in question_list: -> do nothing
                if question in question_list: # keep in list
                    question_list[question] = question_list[question] + 1 # counts occurances of the letter 
        #print(question_list)
        for que in question_list: # check for count of each question to match people in group
            if question_list[que] == lenght_group:
                all_answer.append(que)
        #print(lenght_group)
        #print(all_answer)
        #print(len(all_answer))
        group_questions.append(len(all_answer))
    return group_questions

def sum_list(my_list):
    sum = 0
    for count in my_list:
        sum = sum + count
    return sum

# --- MAIN HERE --- #
#with open("06_Day_Test.txt", "r") as file:
with open("06_Day_Input.txt", "r") as file:
    data = file.read()

group_list = data.split("\n\n")
#print(group_list)

indv_group_list = []
for group in group_list:
    indv_group_list.append(group.split("\n"))
#print(indv_group_list)

#count individual questions awnsered per group
question_per_group_count_01 = individ_count(indv_group_list)
#print(question_per_group_count_01)
#sum list
sum_01 = sum_list(question_per_group_count_01)
print(sum_01)

question_per_group_count_02 = group_count(indv_group_list)
#print(question_per_group_count_02)
sum_02 = sum_list(question_per_group_count_02)
print(sum_02)