"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials 
instead of your passport. While these documents are extremely similar, North Pole Credentials 
aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.
It seems like you're not the only one having problems, though; a very long line has formed for 
the automatic passport scanners, and the delay could upset your travel itinerary.
Due to some questionable network security, you realize you might be able to solve both of 
these problems at the same time.
The automatic passport scanners are slow because they're having trouble detecting which passports have all 
required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) - OPTIONAL

Passport data is validated in batch files (your puzzle input). 
Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. 
Passports are separated by blank lines.

Here is an example batch file containing four passports:
--
The first passport is valid - all eight fields are present. The second passport is invalid - 
it is missing hgt (the Height field).
The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, 
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. 
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, 
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. 
In your batch file, how many passports are valid?

The line is moving more quickly now, but you overhear airport security talking about how passports 
with invalid data are getting through. Better add some data validation, quick!
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
 automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""

# --- FUNCTIONS HERE --- #
def simple_validate(my_dict):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']
    count = 0
    for i in my_dict:
        my_dict[i]['valid'] = 1
        for req in required_fields:
            if req in  my_dict[i]:
                my_dict[i]['valid'] = my_dict[i]['valid'] * 1
            else:
                my_dict[i]['valid'] = my_dict[i]['valid'] * 0
        count = count + my_dict[i]['valid']
    print('All Fields Present:')
    print(count)
    return

def check_range(year_to_check, upper, lower):
        if year_to_check <= upper and year_to_check >= lower:
            return 1
        else:
            return 0

def split_num_unit(my_str):
    for j,c in enumerate(my_str):
        if not c.isdigit():
            break
    num=int(my_str[:j])
    unit=my_str[j:]
    return unit, num

def super_validate(my_dict):
    required_fields = {'byr': {'lower': 1920, 'upper': 2002}, 'iyr': {'lower': 2010, 'upper': 2020}, 
                        'eyr': {'lower': 2020, 'upper': 2030}, 'hgt': {'lower_in': 59, 'upper_in': 76, 'lower_cm': 150, 'upper_cm': 193},
                        'hcl': {'format': '#nnnnnn'}, 'ecl': {'format': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']}, 
                        'pid': {'format': 'nnnnnnnnn'}}
    count = 0

    for i in my_dict:
        #my_dict[i]['valid'] = 1 # intital state true -> prove if false

        #check if feild exists
        for req in required_fields:
            if req in my_dict[i]:

                #check case year
                check_year = ['byr', 'iyr', 'eyr']
                if req in check_year:
                    switch = check_range(int(my_dict[i][req]), required_fields[req]['upper'], required_fields[req]['lower'])
                    my_dict[i]['valid'] = my_dict[i]['valid'] * switch

                # check case height
                if req == 'hgt':
                    unit, num = split_num_unit(my_dict[i][req])
                    if unit == 'in':
                        switch = check_range(num, required_fields[req]['upper_in'], required_fields[req]['lower_in'])
                    elif unit == 'cm':
                        switch = check_range(num, required_fields[req]['upper_cm'], required_fields[req]['lower_cm'])
                    else:
                        switch = 0
                    my_dict[i]['valid'] = my_dict[i]['valid'] * switch

                # check case hex color code
                if req == 'hcl':
                    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                            'a', 'b','c', 'd', 'e','f']
                    if len(my_dict[i][req]) != len(required_fields[req]['format']):
                        switch = 0
                    if my_dict[i][req][0] != '#':
                        switch = 0
                    for n in my_dict[i][req][1:]:
                        if n not in hex:
                            switch = 0
                    my_dict[i]['valid'] = my_dict[i]['valid'] * switch
                               
                # check case eye color
                if req == 'ecl':
                    if my_dict[i][req] not in required_fields[req]['format']:
                        my_dict[i]['valid'] = my_dict[i]['valid'] * 0

                # check case pass id
                if req == 'pid':
                    if len(my_dict[i][req]) != len(required_fields[req]['format']):
                        switch = 0
                    for n in my_dict[i][req]:
                        if not n.isdigit():
                            switch = 0 
                    my_dict[i]['valid'] = my_dict[i]['valid'] * switch

        count = count + my_dict[i]['valid']
        #print('case test' + str(i) + ": " + str(my_dict[i]['valid']))
        #print(my_dict[i]['valid'])
    print('All Fields Verified:')
    print(count)
    
    return

# --- MAIN HERE --- #
#with open('04_Day_Test.txt', 'r') as file:
with open('04_Day_Input.txt', 'r') as file:
    data = file.read()

#print(data)

passport_list = data.split('\n\n')
#print(passport_list)

# read in all passports
passport_dict = {}
for i in range(len(passport_list)):
    passport_dict[i] = {}
    passport_list[i] = passport_list[i].replace('\n',' ')
    pass_split = passport_list[i].split()

    for j in pass_split:
        key_value = j.split(':')
        passport_dict[i][key_value[0]] = key_value[1]

#simple check
simple_validate(passport_dict) # need to run the first one to create the valid key, 
#from that the valid key will be tested, and if a test is negative the key will become 0
super_validate(passport_dict)






