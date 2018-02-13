#Problem Set 1
#Kim, Matthew
#Collaborators:Jeremy Lim

#Part I
import math
def golden_ratio():
    g_ratio = (1 + math.sqrt(5))/2
    return g_ratio
print golden_ratio ()

#Part II

def is_even (input_int):
    lol = int(input_int) % 2
    return lol == 0
print is_even(20)
print is_even(3)

#Part III
import math

def quad_form(a,b,c):
    disc = float(b**2 - (4*a*c))
    sdisc = math.sqrt((disc))
    denominator = float(2*a)
    numerator1 = float((-b + sdisc))
    numerator2 = float((-b - sdisc))
    return numerator1/denominator, numerator2/denominator
def explanation():
    print 'Quadratic Equation values'
    a = float(raw_input('Value of a: '))
    b = float(raw_input('Value of b: '))
    c = float(raw_input('Vale of c: '))
    return quad_form(a,b,c)
print explanation()

#Hello Professor, I really didn't understand how specific you wanted us to be
#when you said "You should always have a prompt for input, explaining what is
#desired". My friend Jeremy interpreted it as putting the Value of the variables
#rather than simply "a=" or "b=" but I thought you meant more explanation.
#I did what I did also because I wanted to try calling a function within a function
#FYI, I originally had the raw inputs not in a function and printed quad_form(a,b,c)
#Have a great weekend!
