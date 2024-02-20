import json

"""These triple quotes are called docstrings"""
"""Like comments (ie. #), they will be ignored by the interpreter and are useful for documenting your code.
They can also span multiple lines like this.
There are standardized ways of documenting your code, but use them how you wish for now."""

with open('listfile.json', 'r', encoding="utf8") as filehandle: #assigns the contents of  listfile.json to the variable titled filehandle
    identifier_list = json.load(filehandle) #interprets filehandle as json and assigns that to the variable titled identifier_list

    """you can quickly 'comment out' a line of code by making it a comment using the shortcut 'command+/' """

    # print(filehandle) #print statements are useful when troubleshooting or stepping through code
    # print(identifier_list) #if a long piece of code isn't working as you expect, break it into smaller pieces
    # exit() #an exit statement like this can be used to end interpretation of code. No lines following this statement will be interpreted

    """the following line prints the number of entries in the variable titled 'identifier list' """
    # print(len(identifier_list))
    #because it is a list of dictionaries, the count is equal to the number of dictionaries

    """the following lines iterate over each entry in 'identifier_list' and prints each one """
    # for x in identifier_list:
    #     print(x)

    """the following lines iterate over each entry in 'identifier_list' and accesses the 'value' key in each and prints that """
    # for x in identifier_list:
    #     print(x['value'])

    """A 'set' is like a list, but it does not permit duplicates"""
    # new_list = [1,2,3,3,4,4,4,5]
    # new_set = set(new_list)
    # print(new_list)
    # print(new_set)

    """How many identifiers are of the type 'csmiles'?"""
    # csmiles_count = 0
    # for x in identifier_list:
    #     if x['type'] == 'csmiles':
    #         csmiles_count += 1
    # print(csmiles_count)


    """Create a list of all of the values of the identifiers of type 'csmiles'?"""


    """How many unique "substance_id"s are in listfile.json?"""
    #hint: One option is to create an empty list and populate it with all of the substance_id's. Then convert it to a set and get the length.


    """How many identifiers are of the type 'csmiles' AND from the source 'pubchem'?"""
    #hint: use two 'if' statements



    """How many values of the type 'othername' match a value of the type 'iupacname'?"""
