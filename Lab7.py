#Lab 7

#1
tup = ('Hello', 'World')
tup[1]
#immutable

#tupl = (50)
#print type(tupl)
#There's only 1 value fam
tupl = (50,)
print type(tupl)

#2


def personal_info():
    info = {}
    a = raw_input('First Name: ')
    b = raw_input('Last Name: ') 
    c = raw_input('Age: ') 
    d = raw_input('Class Year: ')
    if d == '2020':
        d = 'Freshman'
    elif d == '2019':
        d = 'Sophmore'
    elif d == '2018':
        d = 'Junior'
    elif d == '2017':
        d = 'Senior'
    info[1] = a
    info[2] = b
    info[3] = c
    info[4] = d
    return info

def retrieve():
    lol = personal_info()
    print 'Hey, ', lol[1], lol[2]
    print 'You are', lol[3], 'years olds and you are a', lol[4]


#3
#can't have a mutable key
#seperate First and Last name

#4

#a

#adds it
red = {1, 2, 3, 4}
blue = {2, 5, 6, 7, 4}

#b
intersect = red.intersection(blue)
#common items in each set

#c
green = {1,20,30,5}
red.update(green)
# adds uncommon items of green to red

#d
red -={1,2}
#removes it

#5

#countries = {'U.S.': 'Washington, DC',
             'Mexico': 'Mexico City', 'Canada': 'Ottowa'}

#for n in countries:
#    print n
#    print countries[n]



#6
guests = ('Daniel', 'Craig', 'Jennifer', 'Lawrence',
'Ricky', 'Bobby')

guests.replace(3)
guests.append(












    

