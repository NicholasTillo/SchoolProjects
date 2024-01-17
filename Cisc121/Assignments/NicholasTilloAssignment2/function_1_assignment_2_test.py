# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

# First function:

def independent(list_a, list_b):
   '''
      We can say that two lists are independent if no value occupies the
      same position in both lists.  Independent lists are not
      required to have the same length.

         For example, [1,2] and [2,1,3] are independent, and
         [1,2,3]  and [4,2,'a'] are not independent.
         
      Parameters:
         list_a and list_b must be lists

      Returns True if list_a and list_b are independent, and
      returns False if they are not
   '''
   if type(list_a) is not list  or type(list_b) is not list:
      return False
   else:
      min_length = min(len(list_a), len(list_b))
      for i in range(min_length):
         if list_a[i] == list_b[i]:
            return False
      return True
      

def test_independent_1():
   '''If it correctly identifies lists are equal'''
   assert independent([1,[2,3],4],[5,[2,3],6]) == False


def test_independent_2():
   '''If it correctly identifies lists are not equal'''
   assert independent(["Dog", "Cat", ["Bird","Bird"]],["Cow","Horse",["Hamster","Frog"]]) == True


def test_independent_3():
   '''If it thinks that empty sets are the same as full sets'''
   assert independent([1,[],4],[5,[1,2,3,4],6]) == True


def test_independent_4():
   '''If it correctly identifies that the empty set is diffrent from a set with an empty set in it'''
   assert independent([],[[]]) == True


def test_independent_5():
   '''If the program differentiates between strings and intergers, and strings with floats'''
   assert independent(["5",2.0],[5,"2.0"]) == True


def test_independent_6():
   '''If the program differentiates between floats and intergers'''
   assert independent([4],[4.0]) == False