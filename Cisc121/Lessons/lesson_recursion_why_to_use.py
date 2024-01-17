#Flatten the list
z = [1,2,["a","b"], "thing", [[["?"],["!"]],3]]




def flatten(x):
    if type(x) != list:
        print(x)
    else:
        for y in x:
            flatten(y)

flatten(z)