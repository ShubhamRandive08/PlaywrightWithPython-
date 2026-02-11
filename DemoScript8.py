#unique data is stored in set , there is no scope of duplicate values in it
# {123,4,5,5}

empID = {101, 102, 103, 104, 101}
print(empID)

empID.add(201)
print(empID)

empID.discard(201)
print(empID)