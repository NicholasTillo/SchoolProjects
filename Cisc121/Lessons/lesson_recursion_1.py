#Find the largest value in a list of n numbers
list_a = [3,7,1,9,5,4]
max = 3
for val in list_a[1:]:
    if val > max:
        max = list

# 2 scenarios, either the first number is the largest. Or it is the 
#of the rest of the numbers 

#when is the list small enough to have a a definate answer, 
#WHen it has 1 value

def largest(some_list):
    if len(some_list) == 1:
        return some_list[0]
    else:
        temp = some_list[0]
        temp2 = largest(some_list[1:])

        if temp > temp2:
            return temp
        else: 
            return temp2
#These are the two scenarios, either the first number is the largest, or everything else is. 
#This is recursion, each run through there is a reduction of the problem in order to get it to a manageable state. 

#Each run through of the function, it takes a "Snapshot" of the state of the variables at the time. 
#Then it will run through the code again making another "Snapshot", Each run through creates a new some_list, but doesnt destroy the last
#Each of these snapshots of the values are stored in "Domains" or "Storages" 
#At the very end, it returns the last value, returning back 
