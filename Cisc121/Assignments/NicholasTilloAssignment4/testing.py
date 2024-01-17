def prime_factors_rec(n):
#   you write this
    if n < 1:
        return n
    lowestfactor = 2
    while lowestfactor <= n:
        if n % lowestfactor == 0:
            print(lowestfactor, " ", end="")
        return prime_factors_rec(n / lowestfactor)    
    print("\n")

    
dictionary1 = {}
def better_collatz_up_to_n(n):
   ''' print the Collatz Sequence for each value from 1 to n '''
   for i in range(n):
      better_collatz_rec(i+1, "")

def better_collatz_rec(n, finalmessage):
   ''' print the Collatz Sequence for a single integer '''
   finalmessage += " " + str(n)
   if n == 1:
      print(finalmessage)
      return " "
   elif n in dictionary1:
      finalmessage += " " + str(dictionary1[n])
      print(finalmessage)
      return dictionary1[n]
   else:
      if n % 2 == 0:
         value = n // 2
      else:
         value = 3*n + 1
      dictionary1[n] = str(value) + " " + str(better_collatz_rec(value, finalmessage))
      return dictionary1[n]



totalrecursions = 0
def count_routes(n , dict1):
   ''' returns the number of different ways a robot can move forward a total of n metres, when the
       robot can only take steps that go forward either 2 metres or 3 metres. '''
   global totalrecursions
   if n <= 1:
      return 0
   elif n <= 3:
      return 1
   elif n - 2 in dict1:
      return dict1[n-2]
   elif n - 3 in dict1:
      return dict1[n-3]
   else:
      print(n)
      
      totalrecursions += 1
      dict1[n] = count_routes(n - 2, dict1) + count_routes(n - 3,dict1)
      
      print(dict1)
      
      return dict1[n]