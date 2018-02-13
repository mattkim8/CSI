#Lab 5

#1
def integer(n):
    list1 = []
    absolute_int = abs(n)
    for i in range(absolute_int+1, absolute_int*2):
        if i%2==0:
            list1.append(i)
    return list1
        


#2
def integer2(a,b):
    y = integer(a)
    list_copy = y[:]
    x = 0
    for x in y:
        if x%b == 0:
            list_copy.remove(x)
    return list_copy

#3

def mess(n):
    a = []
    b = []
    for i in n:
        if i%2 == 0:
            a.append(n[i])
        else:
            b.append(n[i])
    return b+a
print mess([22, 26, 28, 32, 34, 38, 40])
