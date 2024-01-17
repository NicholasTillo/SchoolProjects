# Name:   <Nicholas Tillo>
# Student Number: <20291255>
# Email:  <20njt4@queensu.ca>

# I confirm that this assignment solution is my own work and conforms to 
# Queen's standards of Academic Integrity

def all_odd_or_even(*args):
    ''' 
    Inputs any number of values, If they are all integers, it will return
    True if all numbers are either even or odd. 
    '''
    if len(args) == 0:
        return False
    for num in args:
        if type(num) is not int or (num % 2 != args[0] % 2):
            return False
    return True


def test_all_odd_or_even_1():
    '''If the program works with even numbers including 0'''
    assert all_odd_or_even(-4,-2,0,2,4) == True


def test_all_odd_or_even_2():
    '''If the program works with odd numbers'''
    assert all_odd_or_even(-5,-3,-1,1,3,5) == True


def test_all_odd_or_even_3():
    '''If the program works with no arguments'''
    assert all_odd_or_even() == False


def test_all_odd_or_even_4():
    '''If the program works with odd and even numbers'''
    assert all_odd_or_even(0,1,2,3,4,5,6,7,8,9,10) == False


def test_all_odd_or_even_5():
    '''If the program can return False with a non integer'''
    assert all_odd_or_even(1,2,3,4,5,6,7.0,8,89) == False


def test_all_odd_or_even_6():
    '''If the program can differenciate between strings and integers'''
    assert all_odd_or_even("Yes") == False


def test_all_odd_or_even_7():
    '''If the program can differenciate between strings and integers'''
    assert all_odd_or_even(1,2,3,"4") == False