#Problem Set 3, Part 1
#Kim, Matthew
#Colab: John King TA meetup thingy
#1
def match(tstring,pstring):
    i = 0
    k = 0
    n = len(tstring)
    m = len(pstring)
    for i in range(0,n):
        if pstring[k] != tstring[i]:
            k = 0
        elif pstring[k] == tstring[i]:
            k = k + 1
            if k >= m:
                return True
            

while True:
    tstring = raw_input('Test String: ')
    pstring = raw_input('Pattern String: ')
    if tstring.lower() == 'qqq' or pstring.lower() == 'qqq':
        break
    elif match(tstring,pstring) == True:
        print "theres a match"
    elif match(tstring,pstring) != True:
        print "no match"
    
