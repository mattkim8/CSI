#6
def greeting():
    name = getName()
    return 'Hello, ' + str(name) + ', nice to meet you!'
    


def getName():
    return raw_input('Please enter your name: ')
    
print greeting()


#7

def isLegal(drink, age):
    if drink == 0:
        print 'True'
    elif age >= 21:
        print 'True'
    elif age < 21 and drink == 1:
        print 'False'
    return

#8

def days():
    a = str(raw_input('What day of the week is it? '))
    if a == 'Monday':
        print 'Mondays suck bro'
    elif a == 'Tuesday':
        print 'Labs today!'
    elif a == 'Wednesday':
        print 'Hump day!'
    elif a == 'Thursday':
        print 'Tomorrow is Friday fam'
    elif a == 'Friday':
        print 'Happy Friday!'
    elif a == 'Saturday':
        print 'Finally!'
    elif a == str(Sunday):
        print 'Enjoy your last day of freedom'
    else:
        print 'that is not a day fam'
    
print days()
