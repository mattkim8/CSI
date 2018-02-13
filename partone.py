# Problem Set 2, Part 1
# Kim, Matthew

a = int(raw_input('Please enter your first integer: '))
b = int(raw_input('Please enter your second integer: '))

def is_divisible(a,b):
    return int(a) % int(b) == 0
result = is_divisible(a,b)

if b == a:
    print 'Both numbers are divisible by each other'
elif result == True:
    print 'The first number is divisible by the second'
elif b % a == 0:
    print 'The second number is divisible by the first one'
else:
    print 'Neither number is divisible by the other one'

