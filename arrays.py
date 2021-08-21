#Title: Array.py Explanation
#This array.py file has been put together to show examples of the different array structures in python.
#The different arrays are:
shortarraytypes = {
    "LIST": "List is a collection which is ordered and changeable. Allows duplicate members.",
    "TUPLE": "Tuple is a collection which is ordered and unchangeable. Allows duplicate members.",
    "SET": "Set is a collection which is unordered and unindexed. No duplicate members",
    "DICTIONARY": "Dictionary is a collection which is ordered* and changeable. No duplicate members.",
}
longarraytypes ={
    "LIST": """
            Lists are used to store multiple items in a single variable. 
            Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, 
            Set, and Dictionary, all with different qualities and usage. 
            Lists are created using square brackets:
            ------------------------------------------
            >>thislist = ["apple", "banana", "cherry"]
            >>print(thislist)
            <<['apple', 'banana', 'cherry']>>
            ------------------------------------------
            List have these attributes:
            indexed
            ordered
            changeable
            allows duplicates
            """,
    "TUPLE": """
            Tuples are used to store multiple items in a single variable.
            Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, 
            Set, and Dictionary, all with different qualities and usage.
            A tuple is a collection which is ordered and unchangeable.
            Tuples are written with round brackets:
            ------------------------------------------
            >>thistuple = ("apple", "banana", "cherry")
            >>print(thistuple)
            <<('apple', 'banana', 'cherry')>>
            ------------------------------------------
            Tuple have these attributes:
            indexed
            ordered
            un-changeable
            allows duplicates
            """,
    "SET": """
            Sets are used to store multiple items in a single variable.
            Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, 
            Tuple, and Dictionary, all with different qualities and usage.
            A set is a collection which is both un-ordered and un-indexed.
            Sets are written with curly brackets:
            ------------------------------------------
            >>thisset = {"apple", "banana", "cherry"}
            >>print(thisset)
            <<{"apple", "banana", "cherry"}>>
            ------------------------------------------
            Set have these attributes:
            non-indexed
            un-ordered
            un-changeable
            disallows duplicates
            """,
    "DICTIONARY": """
            Dictionaries are used to store data values in key:value pairs.
            A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
            Dictionaries are written with curly brackets, and have keys and values:
            ------------------------------------------
            >>thisdict = {
                "brand": "Ford",
                "model": "Mustang",
                "year": 1964
            }
            >>print(thisdict)
            <<{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}>>
            ------------------------------------------
            Dictionary have these attributes:
            non-indexed
            ordered
            changeable
            disallows duplicates
            """,
}
learnarray = 0
while learnarray == 0:
    learnarraylength = input("Would you like short or long descriptions?: ").upper()
    if learnarraylength.find("S") == 0:
        shortlearnarrays = 0
        while shortlearnarrays == 0:
            shortselectedarray = input(
                "Select one of the following arrays to lean about; List, Tuple, Set, Dictionary: "
            ).upper()
            if (shortselectedarray == "LIST" or shortselectedarray == "TUPLE" or
                shortselectedarray == "SET" or shortselectedarray == "DICTIONARY"):
                print("A description of [" + shortselectedarray + "] will be shown below:")
                print(shortarraytypes[shortselectedarray])
                shortlearnmorearray = input("Do you want to learn about another type? (Y/N): ").upper()
                if shortlearnmorearray.find("N") == 0: shortlearnarrays = 1
            elif shortselectedarray.find("N") == 0:
                print("Okay we'll skip this")
                shortlearnarrays = 1
            else:
                print("You need to enter an array type.")
    elif learnarraylength.find("L") == 0:
        longlearnarrays = 0
        while longlearnarrays == 0:
            longselectedarray = input(
                "Select one of the following arrays to lean about; List, Tuple, Set, Dictionary: "
            ).upper()
            if (longselectedarray == "LIST" or longselectedarray == "TUPLE" or
                longselectedarray == "SET" or longselectedarray == "DICTIONARY"):
                print("A description of [" + longselectedarray + "] will be shown below:")
                print(longarraytypes[longselectedarray])
                longlearnmorearray = input("Do you want to learn about another type? (Y/N): ").upper()
                if longlearnmorearray.find("N") == 0: longlearnarrays = 1
            elif longselectedarray.find("N") == 0:
                print("Okay we'll skip this")
                longlearnarrays = 1
            else:
                print("You need to enter an array type.")
    elif learnarraylength.find("N") == 0:
        print("Okay you're done")
        learnarray = 1
    else:
        print("Please try to answer this question again")
print("Code Finished Executing")
