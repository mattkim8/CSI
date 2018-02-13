#Problem Set 5, Part 1
#Kim, Matthew


def list_min(a):
    temp = a[0]
    for i in a:
        if i < temp:
            temp = i
    return temp

def list_sort(b):
    x = []
    y = []
    z = list(b)
    q = []
    for i in range(0,len(b)):
        num = list_min(z)
        y.append(b.index(num))
        x.append(num)
        z.remove(num)
    q.append(x)
    q.append(y)
    return q

def merge_lists(firstlist,secondlist):
    #clone lists for input purposes
    thirdlist = firstlist + secondlist
    fourthlist = []
    for n in range(0,len(thirdlist)):
        secondnum = list_min(thirdlist)
        fourthlist.append(secondnum)
        thirdlist.remove(secondnum)
    return fourthlist

