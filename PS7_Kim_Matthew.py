#Problem Set 7
#Kim, Matthew
#Collaborators: Lim, Jeremy

def recursive_count(string, char):
    if char not in string:
        return 0
    if char == string[0]:
        return 1+recursive_count(string[1:], char)
    return recursive_count(string[1:], char)

def depth_first(nested_list):
    if nested_list == []:
        return nested_list
    if isinstance(nested_list[0], list):
        return depth_first(nested_list[0]) + depth_first(nested_list[1:])
    return nested_list[:1] + depth_first(nested_list[1:])



def realmath(n):
    J = 1
    if n == 0:
        return 3
    elif n == 1:
        return 7
    else:
        x = 3
        k = 2*x+1
        while J != n:
            y = (2 * k+1)
            k = y
            J += 1
        return y



    

