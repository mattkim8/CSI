#3
def recursivething(a,b):
    if a < b:
        return 0,a
    new_tuple = (recursivething(a-b,b))
    return ((new_tuple[0]+1), new_tuple[1])

print recursivething(5,3)
    
#7
#def paren(a):
#    if a = 
