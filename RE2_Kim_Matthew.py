#Review Exercise 2
#Kim, Matthew
#Collaborators Lim, Jeremy

def positive_power(x,n):
    num = 1.0
    for n in range(0,int(n)):
        num = num*x
    return float(num)


        
def power(x,k):   
    if k>0:
        return positive_power(x,k)
    elif k<0:
        return 1/(positive_power(float(x),float(-1)*k))
    else:
        return 1
