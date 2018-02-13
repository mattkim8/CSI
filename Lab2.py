#1
x = 24.
y = (1./3)

print x/3
print x*y
#They didn't have the same value because one's a float and the other's an interger
#change them both to floats

#2
def hello():
    name = raw_input("What's your name?")
    greeting = "Hello "+ name + "!"+ " Nice to meet you!"
    return greeting
print hello()


#3
def average(x,y,z):
    avg = (x + y + z)/3.
    return avg
print average(2,4,6)

#4
def leap_year():
    year = raw_input("Put year here: ")
    leapyear = int(year) - (int(year) % 4) +4
    return leapyear
print leap_year()

#5
import math
def hypotenuse(a,b):
    lol = math.sqrt((int(a)**2+int(b)**2))
    return lol
print hypotenuse(3,4)

#6
def height():
    h = raw_input("What's your height?")
    return h + " inches"
h = 20
print height()
print h

#prints 20 cuz variables are in the function and localized

#7
import math

a = raw_input("What's your height fam?(in feet) ")
b = raw_input("How far away is the thing fam?(in feet) ")
def triangle(a,b):
    distance = math.sqrt((int(a)**2) + (int(b)**2))
    return distance
print triangle(a,b)


