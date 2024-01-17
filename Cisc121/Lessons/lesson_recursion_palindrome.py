def is_palindrone_recursive(S):
    if len(S) <= 1:
        return True
    else:
        return (S[0] == S[-1]) and is_palindrone_recursive(S[1:-1])

#Wow very nice :) Very compressed

"""
Can be done like:
def is_palindrone_recursive(S):
    return (len(S) <= 1) or ((S[0] == S[-1]) and is_palindrone_recursive(S[1:-1]))

Or like:
def is_palindrone(S):
    return(is_palindrone_2(S, 0, len(s)-1))
USes a helper function to set up for the recursive 

def is_palindrone_2(S, first, last):
    if(last - fisrt) <= 0:
        return True
    else:
        return (S[first] == S[last]) and is_palindrone_2(S, first + 1, last - 1)


Because it passes in the whole string, it doesnt make a copy, makes it must faster. 

"""