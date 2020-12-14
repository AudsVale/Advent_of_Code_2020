"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; 
the easiest way down to the coast from here is via toboggan.
The shopkeeper at the North Pole Toboggan Rental Shop is having 
a bad day. "Something's wrong with our computers; we can't log in!" 
You ask if you can take a look.
Their password database seems to be a little corrupted: 
some of the passwords wouldn't have been allowed by the Official 
Toboggan Corporate Policy that was in effect when they were chosen.
To try to debug the problem, they have created a list 
(your puzzle input) of passwords (according to the corrupted database) 
and the corporate policy when that password was set.
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the 
lowest and highest number of times a given letter must appear for the password to be valid. 
For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no 
instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, 
both within the limits of their respective policies.
How many passwords are valid according to their policies?

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan 
Corporate Authentication System is expecting.
The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old
 job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
Each policy actually describes two positions in the password, where 1 means the first character, 
2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the 
purposes of policy enforcement.
Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""

# --- Functions Here --- #

def count_valid_oldShop(entry_array):
    count = 0
    for entry in entry_array:
        low_bound = entry[0]
        high_bound = entry[1]
        letter_to_count = entry[2]
        password_to_check = entry[3]
        
        count_inner = 0
        for letter in password_to_check:
            for i in letter:
                if i == letter_to_count:
                    count_inner = count_inner + 1 

        if count_inner >= low_bound and count_inner <= high_bound:
            count = count + 1

    return count

def count_valid_newShop(entry_array):
    count = 0
    for entry in entry_array:
        position_1 = entry[0] - 1 # fix for lack of index
        position_2 = entry[1] - 1
        letter_to_check = entry[2]
        password_to_check = entry[3]
        
        if password_to_check[position_1] == letter_to_check or password_to_check[position_2] == letter_to_check:
            if password_to_check[position_1] != password_to_check[position_2]:
                count = count + 1

    return count


# --- Main Here --- #

# import my list of lists
passwords = []
f = open('./02_Day_Input.txt', 'r')

for line in f:
    split_up = []
    # split line into list with numberA, numberB, letter, passcode
    split_numA = line.split('-')
    split_up.append(int(split_numA[0]))

    split_numB = split_numA[1].split(' ',1)
    split_up.append(int(split_numB[0]))

    split_letter = split_numB[1].split(': ')
    split_up.append(split_letter[0])

    split_pass = split_letter[1].split('\n')
    split_up.append(split_pass[0])

    # append line list to total passwords array
    passwords.append(split_up)

#print(passwords)
test_array = [[1, 3, 'a', 'abcde'], [1, 3, 'b', 'cdefg'], [2, 9, 'c', 'ccccccccc']]

valid_count_old = count_valid_oldShop(passwords)

valid_count_new = count_valid_newShop(passwords)

print(valid_count_old)
print(valid_count_new)


