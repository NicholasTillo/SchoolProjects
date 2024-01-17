'''
Assumes an ordering exists on the values. 

Partial ordering - Sometimes not all values can be compared.
Python comes with sorting functions, the base .sort() and using a lambda functions 
All these can be done non recursively  
'''

#Merge Sort - 


#Bubble sort and quick sort are both really bad, only use merge sort. 
#Split the list into 2 equal sized parts, 
#Sort the left side, sort the right side.
#Merge the two sides. This is done by comparing the lowest left side and the lowest right side. 
#then placing the smaller of the two into the new sorted list, then repeat comparison. 

def merge_sort(a_list):
    return rec_merge_sort(a_list, 0, len(a_list)-1)


def rec_merge_sort(a_list, first, last):
    if first > last:
        return []
    elif first == last:
        return [a_list[first]] #Our goal is to return a copy of a_list, so we cant just reutn a_list, cause it would just be a copy.ef
    elif last == first + 1:
        if a_list[first] <= a_list[last]:
            return a_list[:]
        else:
            return [a_list[last],a_list[first]]
    else:
        leftsorted = rec_merge_sort(a_list, first, (first+last) //2)
        rightsorted = rec_merge_sort(a_list, (first+last)//2 + 1, last)
        return merge(leftsorted, rightsorted)
    

def merge(a_list, b_list):
    f1 = 0
    f2 = 0
    l1 = len(a_list) - 1
    l2 = len(b_list) - 1
    merged_list = []
    while f1 <= l1 and f2 <= l2:
        if a_list[f1] <= b_list[f2]:
            merged_list.append(a_list[f1])
            f1 += 1
        else:
            merged_list.append(b_list[f2])
            f2 += 1
    if f1>l1:
        merged_list.extend(b_list[f2:])
    else:
        merged_list.extend(a_list[f1:])
    return merged_list
print(merge_sort([5,2,3,1,6,3,7,9,4]))



