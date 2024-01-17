#Consider x^y A non negative integer

def exponent_recursive(x,y):
#First solve a smaller program, and then solve another with that solution
#We can reduce x^y to x * x^y-1
    if y == 0:
        return 1
    else:
        return x * exponent_recursive(x, y-1)


def exponent_recursive_2(x,y):
#Split it in half, For example, split x^8 into two sets of x^4, Then we can solve for one of them, and then multiply by itself. 
#Then we can split that into 2 x^2 to be even more efficient. 
#This brings an issue when it becomes odd though, But we can just seperate one of the x's off in order to get a even exponent.
#For example, x^9 can be x^8 * x

#(((x^2)^2)^2)
    if y==0:
        return 1
    else:
        temp = exponent_recursive_2(x,y//2)
        result = temp * temp
        if y % 2 == 0:
            return result
        else:
            return result * x
#Splitting the problem in half is a great tool for efficiency. 
print(exponent_recursive(2,5))
print(exponent_recursive_2(2,5))


