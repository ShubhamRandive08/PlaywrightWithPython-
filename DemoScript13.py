#unique data is stored in set , there is no scope of duplicate values in it
# {123,4,5,5}

empID = {101, 102, 103, 104, 101}
stuID = {201, 202, 203, 103, 102}
names = {"Alice", "Bob", "Charlie", "Alice"}

"""
lets add multiple values to set: 
update() method for which we will pass on desired values as a list 

discard : to remove a specific value from set
foir suppose if the value isnt there in the set what will happen?

remove() : to remove a specific value from set, if the value isnt there in the set then it wil throw error
pop()

del listname --> deleting entire list
del listname[index] --> deleting specific index value from list

set isnt assocated based on index position --> 
clear : 
len --> 
copy data from 1 set to another set
i want to egt common values from 2 sets : intersection()
i want to get all unique values from 2 sets : union()

"""

set3 = empID.union(stuID)
print(set3)
# set3 = empID.intersection(stuID)
# set3 = empID & stuID
# print(set3)

# ids = empID.copy()
# ids = empID



# if "suren" in names:
#     print("suren is present in names set")
# else:
#     print("suren is not present in names set")

# del empID
# empID.clear()
# print(empID)

# empID.pop()
# print(empID)


# empID.discard(201)
# empID.remove(201)
# print(empID)
# empID.update([901, 902, 903])
# print("After update empID:", empID)