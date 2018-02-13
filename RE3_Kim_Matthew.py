#Review Exercise 3
#Kim, Matthew
#Collaborators Lim, Jeremy


def flatten(a):
    x = []
    b = len(a)
    n = 0
    for n in range(b-1, b):
        for i in range(0,n+1):
            x = x + a[i]
            n+=1
    return x
print flatten([['a', 'BC'], ['b'], ['lol'], ['CS'], [4,5,6,7]])
