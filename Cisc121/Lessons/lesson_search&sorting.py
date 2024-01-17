#Searching and sording
#Divide & Conqour, A common problem solving technique, divide the problem into smaller problems and solve those. 
#x^y = x^(y/2) * x^(y/2), split the problem into two, solve one, and then copy the result. 
#In a sorted array / Python List:  L
#Find x's position in L (If its there) 
#The key to making search efficient, is to elimate objects we know are incorrect, without actually checking them. 
#To search a list, find the middle, then check if that number is larger, smaller, or equal to x, the desired output. 
#Depending on the answer, we can eliminate half of the list from being x
#Common Name Binary Search

def bin_search(a_list, target):
    return b_s_r(a_list, target, 0, len(a_list)-1)

def b_s_r(a_list, target, first, last):
    if first > last:
        return -1
    else:
        mid = (first + last) // 2
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            return b_s_r(a_list, target, first, mid)
        else:
            return b_s_r(a_list, target, mid + 1, last)