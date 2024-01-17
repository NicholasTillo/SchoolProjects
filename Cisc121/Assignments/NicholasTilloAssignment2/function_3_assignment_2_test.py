# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# Third function:

def binary_string(n):
   '''parameter:
         n - integer
         
      returns a string of "0"s and "1"s giving the binary representation of n
      returns None if n is not an integer
   '''
   
   if type(n) is not int:
      return None
   else:
      if n == 0:
         return '0'
      else:
         negative = (n < 0)
         n = abs(n)
         bin_string = ''
         while n != 0:
            if n % 2 == 1:
               bin_string = '1' + bin_string
            else:
               bin_string = '0' + bin_string
            n = n // 2
         if negative:
            bin_string = '-' + bin_string
         return  bin_string  


def test_binary_string_1():
   '''Testing if inputting a string creates a crash'''
   assert binary_string("4") == None


def test_binary_string_2():
   '''Testing the positivie integer option'''
   assert binary_string(10) == "1010"


def test_binary_string_3():
   '''Testing the negative integer option'''
   assert binary_string(-10) == "-1010"


def test_binary_string_4():
   '''If the program correctly uses an inputted 0'''
   assert binary_string(0) == "0"


def test_binary_string_5():
   '''Testing if inputting a float creates a crash'''
   assert binary_string(4.0) == None


def test_binary_string_6():
   '''Testing if inputting a float creates a crash'''
   assert binary_string([1,2,3,4]) == None