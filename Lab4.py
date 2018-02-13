#1
def triangle():
    for n in range(1,6):
        print '*'*n

def triangle2(k):
    for n in range(1,k+1):
        print '*' * n
        
#2
def aFunction():
    aNum = 0
    while (aNum<99):
        aNum = aNum + 2
        print aNum
        
    return None
#Don't define aNum = 0 inside the while function
#Change 101 to 99 since 100+2 is 102 while 98+2 is 100

#3

def password(x):
    msg = raw_input('Please enter your password')
    while msg != x:
        print 'incorrect password'
        msg = raw_input('Please enter your password')
    if msg ==x:
        print 'correct'
        

#4

def factorial(num):
    fact = 1
    for n in range(1, num+1):
        fact = fact * n
    return fact

print factorial(5)

def factorial2(number):
    fac = 1
    while fac <= number:
        number =  number * fac
        fac += 1
        return number
    
        
        



