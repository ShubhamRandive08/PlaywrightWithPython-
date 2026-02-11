# For loop : It is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Syntax :
# for variable in sequence:
#     statement(s)

# for loop
# print numbers from 0 to 4
# for i in range(5):
#     print(i)

# Now i want to start from 2 to 10
# for i in range(2,11):
#     print(i)

empName = 'Shubham'
def printData():
     global empName
     empName = 'Bhag'

printData()

print(empName)