#Lab 6

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
    for i in range(0,len(n)):
        if i%2 == 0:
            a.append(n[i])
        else:
            b.append(n[i])
    return b+a
print mess([22, 26, 28, 32, 34, 38, 40])

#4
def mutability():
    string_name = 'name'
    list_name = ['n', 'a', 'm', 'e']
    string_name.replace('a', '')
    list_name.remove('a')
    print string_name
    print list_name
    return None

# I thought the output would be 'n', '', 'm', 'e'
# Could fix it by getting rid of the remove method

#5

def only_evens(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b
#6
#def add_color(color_list, color):
#    if color in color_list:
#            if raw_input("color's already in, wanna delete?") == 'y':
#                color_list.remove(color)
#                return color_list
#    if color not in color_list:
#        color_list.append(color)
#    return color_list

def add_color(color_list, color):
    if color in color_list:
            if raw_input("color's already in, wanna delete?") == 'y':
                color_list.remove(color)
                return color_list
    if color not in color_list:
        color_list.append(color)
        return color_list[::-1]
    if len(color_list)>3:
        color_list.remove #list indexing?




    
color_list = ['Red', 'Blue', 'Yellow']

#7




    
