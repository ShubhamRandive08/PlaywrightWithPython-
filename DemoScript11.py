names = ["suren", "ramya", "daya", "neha", "buren","abdul", "kumar"]
dupliate_names = []
empID = [101,102,103,104,105]
# print(names)

empData = ["ramya", 25, "developer", 50000.50]

"""
ordered 
mutable
allows duplicate values
index based operations --> index 1 it will be getting the 2nd value from the list
it accepts index from -1 also -1 means last value -2 means 2nd last value
i dont want only 1 value , i want to egt multiple values from the list
slicing operation --> start index : end index (end index is exclusive)
i want to verufy whether a name or value is presnt in the list or not
in operator : returns boolean value True/False
count method : to get how many times a value is present in the list
ascending order : sort() method
descending order : sort(reverse=True)
reverse operation : reverse() method : to reverse the entire list but all the list items should be in order
then thisd reverse will work like a sorting in descending order
remove a value from the list using index : pop() method
del keywrod followed by listname : deletes the entire list
del keyword followed by listname[index] : deletes a specific value based on index position
copy method : to create a copy of the existing list
list() function : to create a list from the existing iterable object like tuple, set, dictionary etc

"""
# print(names+empID)
names.extend(empData) # to names we are adding empData lst value
print(names)
# dupliate_names=names.copy()
# print(names)
# dupliate_names =list(names)
# print(dupliate_names)



# del names # deletes the entire list
# del names[2]   # deletes a specific value based on index position
# print(names)


# names.remove("suren")
# names.pop(2) # removes the value based on index position
# print(names)



# names.sort() # ascending order --> rearrange the list in ascending order
# names.reverse() # reverse the entire list --> descending order
# print(names)




# print(names.count("suren"))
# names.sort() # ascending order --> rearrange the list in ascending order
# names.sort(reverse=True)
# print(names)



# if "surendra" in names:
#     print("suren is present in the list")
# else:
#     print("suren is not present in the list")



# print(names[0:2]) # getting 1st and 2nd value




# print(names[-1])
# print(names[-2])
# print(names[-3])

