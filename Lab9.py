#Lab 9

def power(a,b):
    if b == 0:
        return 1
    return a * power(a,b-1)


def bin_rep(a):
    if a == 0:
        return []
    return bin_rep(a/2) + [a%2]

##def power_set(a):
##    if len(a) == 0:
##        return {()}
##    for char in a:
##        return tuple(bin_rep(char)) + (char+1)
##print power_set((1,2))
    
    
def super_digit(a):
    if len(str(a)) == 1:
        return a
    for char in range(0,len(str(a))):
        return super_digit(int(a[char]))
print super_digit(9875)
