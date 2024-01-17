# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Part 1
   
def exponent_rec(x, y):
   ''' compute x^y, where y is a positive integer '''
   if y < 1:
      return 1
   else:
      return x * exponent_rec(x,y - 1)
print(exponent_rec(3, 7))

# Problem 2:

def sublist_sum_rec(a_list, target):
   ''' determine if list a_list has a consecutive sub-list that sums to target '''
   if len(a_list) < 1:
      return False
   elif target == sublist_sum_rec_help(a_list,target):
      return True
   else:
      return sublist_sum_rec(a_list[1:], target) 


def sublist_sum_rec_help(a_list, target):
   '''Takes a list and figures out if there is a sublist within it.'''
   if len(a_list) < 1:
      return 0
   elif target > 0:
      target -= a_list[0]
      return a_list[0] + sublist_sum_rec_help(a_list[1:], target)
   else:
      return 0


print(sublist_sum_rec([4, 9, 3, 1, 7, 2, 4], 13)) 

# Problem 3:

def prime_factors_rec(n, lowestfactor):
   ''' print the prime factorization of n'''
   if n < 1 or lowestfactor > n:
      return n
   if n % lowestfactor == 0:
      print(lowestfactor, " ", end="")
      return prime_factors_rec(n / lowestfactor, lowestfactor)
   else:
      return prime_factors_rec(n, lowestfactor + 1)
            
    
prime_factors_rec(126,2)
print("\n")

# Problem 4:    

def matching_parentheses_rec(a_string):
   '''Takes a string and passes it to the recursive
   string, then takes its output and translates it to
   True Or False'''
   value = matching_parentheses_rec_work(a_string)
   if value == 0: 
      return True
   else: 
      return False


def matching_parentheses_rec_work(a_string):
   '''determine if string a_string contains properly
      matched parentheses (i.e. each right parenthesis
      is matched with an earlier left parenthesis)'''
   if len(a_string) < 1:
      return 0
   else:
      value = matching_parentheses_rec_work(a_string[:-1])
      if a_string[0] == "(":
         value += 1 
      elif a_string[0] == ")":
         value -= 1
      return value 


print(matching_parentheses_rec("abc((ef)gh(ij()k)lm((()n)opq())rst)uvw(xyz)"))

# Part 2:

# Each of these recursive functions is inefficient due to duplicated
# effort.  Improve them by storing the solutions to smaller problems that
# are needed repeatedly.

# Problem 5

def better_collatz_up_to_n(n):
   ''' print the Collatz Sequence for each value from 1 to n '''
   dictionary1 = {}
   for i in range(1, n+1):
      better_collatz_rec(i, "", dictionary1)


def better_collatz_rec(n, finalmessage, dic):
   ''' print the Collatz Sequence for a single integer '''
   finalmessage += " " + str(n)
   if n == 1:
      print(finalmessage)
      return " "
   elif n in dic:
      finalmessage += " " + str(dic[n])
      print(finalmessage)
      return dic[n]
   else:
      if n % 2 == 0:
         value = n // 2
      else:
         value = 3*n + 1
      dic[n] = str(value) + " " + str(better_collatz_rec(value, finalmessage, dic))
      return dic[n]


better_collatz_up_to_n(10)

# Problem 6
def count_routes(n , dict1):
   ''' returns the number of different ways a robot can move forward a total of n metres, when the
       robot can only take steps that go forward either 2 metres or 3 metres. '''
   if n <= 1:
      return 0
   elif n <= 3:
      return 1
   elif n - 2 in dict1:
      if n - 3 in dict1:
         return dict1[n-2] + dict1[n-3]
      elif n - 3 in dict1:
         return dict1[n-2] + count_routes(n - 3,dict1)
         
   elif n - 3 in dict1:
      return dict1[n-3] + count_routes(n - 2, dict1)

   else:
      dict1[n] = count_routes(n - 2, dict1) + count_routes(n - 3,dict1)
      return dict1[n]


print(count_routes(18 ,{}))

# Part 3

# Problem 7

def binary_search_non(sorted_list, target):
   ''' 
      returns the location of target in a_list if target is in a_list, 
      returns -1 if target is not in a_list 
      a_list must be sorted prior to calling this function
   '''
   total = 0
   mid = 100
   while mid > 1:
      mid = len(sorted_list) // 2
      if sorted_list[mid] == target: 
         total += mid
         return total
      elif sorted_list[mid] <= target:
         sorted_list = sorted_list[mid:]
         total += mid
      elif sorted_list[mid] >= target:
         sorted_list = sorted_list[:mid]
   return -1


print(binary_search_non([4, 7, 12, 15, 23, 28, 33, 34, 35, 100, 5280, 5281], 100))

# Problem 8

def gcd(a,b):
   ''' returns the greatest common divisor of a and b, which must be positive integers '''
   if b == 0:
      return a
   else:
      return gcd(b, a % b)
      
# Example of use
print(gcd(8,20))

def greatest_divisor(a,b):
   ''' returns the greatest common divisor of a and b, which must be positive integers '''
   for x in range (1, a+1):
      if a % x == 0 and b % x == 0:
         gcf = x 
   return gcf 

print(greatest_divisor(8,20))