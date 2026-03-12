import re

"""
# STEP 1

A CAS registry number consists of three groups of numbers separated by hyphens. 
The first group consists of 2-7 digits, the second is 2 digits, and the last group is a single digit .
Look at the following examples and decide whether they look like valid CAS numbers based only 
on the above criteria:
71329-38-9
2345-4-1
123456789-14-1
123-45-6
789-45-34
"""

casrn = "71329-38-9"

caspatt = re.compile(r'REGEX PATTERN HERE') #compiles the regex pattern into a pattern object that we can use to check for in text
test = caspatt.search(casrn) #uses the regex pattern object to check the input for a match

if test:
    print(test.group() + " might be valid")
else:
    print(casrn + " is invalid")

"""
STEP 2
Convert that script into a definition that can be more easily reused as needed.
"""

def casrn_check(casrn):
    cas = re.compile(r'REGEX PATTERN HERE')
    valid = cas.search(casrn)
    if valid:
        output = valid.group() + " might be valid"
    else:
        output = str(valid) + " is invalid"
    return output

# casrn_output = casrn_check("71329-38-9")
# print(casrn_output)


"""
STEP 3
Now iterate over and check each of the CASRN numbers
"""

# CASRN_list = ['71329-38-9', '2345-4-1', '123456789-14-1', '123-45-6', '789-45-34']
# for input in CASRN_list:
#     print(CASRN_check(input))





"""xxxkeyxxx r'(\d{2,7})-(\d\d)-(\d)' """
"""xxxkeyxxx r'((?<!\d)\d{2,7})-(\d\d)-(\d)(?!\d)' """