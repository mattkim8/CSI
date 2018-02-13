#Lab 3
#Kim, Matthew
import math


def square(a):
    return a*a


def operation (a,b):
    x = square(a) + square(b)
    return x


#1. It should end in a return statement

#2.
def minus(c,d):
    y = square(c-d)
    return y


#3
def myGCD(a, b):
    while b:
        a, b = b, a%b
    return a


def GCD():
    a = int(raw_input('The First interger is '))
    b = int(raw_input('The Second interger is '))
    return myGCD(a,b)
print GCD()

#4

def MyPow(a,b=2):
    return a**b
#5

def isEven(a):
    print a%2==0
    return





