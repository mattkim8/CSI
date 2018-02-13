#1
peas = 1.05
tuna = 2.25
ham = 3.45

print 'peas', int(peas), 'dollar'
print 'tuna', int(tuna), 'dollar'
print 'ham', int(ham), 'dollar'

#2

letters = "Computer Science"
print letters [3:6]
print letters [2] + letters [4] + letters [5] + letters[6]
print letters [9] + letters [11] + letters [13]


#3

words = "TheQuickBrownFox"
print words [0:3], words [3:8], words [8:13], words[13:17]

#4

numbers = "123456"

#a
product = int(numbers[0]) * int(numbers[1]) * int(numbers[2]) * int(numbers[3]) * int(numbers[4]) * int(numbers[5])
print product
#b
print product/7
print float(product/7)
#c
import math
print math.factorial(6)

#5
import math
def cone_volume (radius,height):
    volume = math.pi * radius**2 * height/3
    return volume, int(volume)
print cone_volume(3.5,5.2)

#6

age = raw_input ("Input your age: ")
bday = 2016 - int(age)
print bday

#7

import math
my_sin = math.sin (math.pi / 2)
my_cos = math.cos (math. pi / 2)
my_tan = my_sin / my_cos
print my_tan

#8

print 17

print 219/66
print "3 is the GCD"





