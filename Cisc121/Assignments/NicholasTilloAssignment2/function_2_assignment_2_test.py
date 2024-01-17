# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity
      
# Second function:   

def primes_up_to_n(n):
   '''parameter :
          n - integer
          
   returns a list of all primes <= n
   returns None if n is not an integer
   '''
   if type(n) is not int:
      return None
   else:
      list_of_primes = []
      for potential_prime in range(2,n+1):
         #print("potential prime",potential_prime)
         could_be_prime = True
         done = False
         possible_divisor = 2
         while could_be_prime and possible_divisor < potential_prime:
            #print("\tpossible divisor",possible_divisor)
            if potential_prime % possible_divisor == 0:
               could_be_prime = False
               is_prime = False
            else:
               possible_divisor += 1
               
         if possible_divisor == potential_prime:
            list_of_primes.append(potential_prime)
            
      return list_of_primes


def test_primes_up_to_n_1():
   '''If the program correctly uses an inputted positive number'''
   assert primes_up_to_n(20) == [2,3,5,7,11,13,17,19]


def test_primes_up_to_n_2():
   '''If the program correctly uses an inputted negative number'''
   assert primes_up_to_n(-20) == []
   

def test_primes_up_to_n_3():
   ''' If the program correctly uses an inputted 0'''
   assert primes_up_to_n(0) == []


def test_primes_up_to_n_4():
   '''Testing if inputting a string creates a crash'''
   assert primes_up_to_n("4") == None


def test_primes_up_to_n_5():
   '''If the program correctly uses the lowest possible prime number'''
   assert primes_up_to_n(2) == [2]


def test_prime_up_to_n_6():
   '''Testing if inputting a float creates a crash'''
   assert primes_up_to_n(4.0) == None


def test_prime_up_to_n_7():
   '''Testing if inputting a list creates a crash'''
   assert primes_up_to_n([1,2,3,4]) == None


def test_primes_up_to_n_8():
   '''If the program correctly uses an inputted 1'''
   assert primes_up_to_n(1) == []