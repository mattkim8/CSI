#Problem Set 5, Part II
#Kim, Matthew



# you might want to use one of the functions you defined in the previous part
# of this pset. This is why we're importing that file here. If you want to use
# the list_sort function in the other file, you should use the dot notation,
# i.e., listops.list_sort(....) Make sure this file, the listops file, and the
# part2helper.py are all in the same folder.
import listops
import part2helper # importing this file to get the nested list defined there.


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






# All your function definitions should be before this line and after the
# import lines.

# __main__
# Please do **not** remove the following line. The variable tasks is the
# nested list storing the tasks.
tasks = part2helper.tasks 

# Have the rest of your main program here.


    

def print_task(tasks,b):
    months = ['','Jan', 'Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
    q = []
    lastlist = []
    for n in range(0,len(tasks)):
        if b[0] == tasks[n][1] and b[1] == tasks[n][2]:
            q.append(tasks[n])
    result_printtask = q
    return result_printtask
    
def order(a):
    x = []
    a = print_task(tasks,a)
    for i in a:
        x.append(i[3])
    result_order = list_sort(x)
    return result_order

def starttime(a):
    x = []
    b = order(a)
    result_printtask = print_task(tasks,a)
    for i in b[1]:
        x.append(result_printtask[i][3])
    return x

def minutes(a):
    x = []
    b = order(a)
    result_printtask = print_task(tasks,a)
    for i in b[1]:
        x.append(result_printtask[i][4])
    return x

def task(a):
    x = []
    b = order(a)
    result_printtask = print_task(tasks,a)
    for i in b[1]:
        x.append(result_printtask[i][0])
    return x

def description(a):
    x = []
    b = order(a)
    result_printtask = print_task(tasks,a)
    for i in b[1]:
        x.append(result_printtask[i][6])
    return x

def duration(a):
    x = []
    b = order(a)
    result_printtask = print_task(tasks,a)
    for i in b[1]:
        x.append(result_printtask[i][5])
    return x

def convert_to_minutes(a):
    hour = starttime(a)
    minute = minutes(a)
    x = [hour, minute]
    time = []
    for i in range(0,len(x[1])):
        time.append(x[0][i]*60 + x[1][i])
    return time

def newtime(a):
    start_time = convert_to_minutes(a)
    newtime = []
    for i in range(0,len(start_time)):
        newtime.append(start_time[i] + duration(a)[i])
    return newtime

def newtime2(a):
    newtime2 = []
    newtimet = newtime(a)
    for n in range(0,len(newtimet)):
        newtime2.append(int(newtimet[n]/60))
    return newtime2

def newminutes(a):
    newminutes = []
    newtimed = newtime(a)
    newtimeo = newtime2(a)
    for j in range(0,len(newtimed)):
        newminutes.append((newtimed[j]/60.0 - newtimeo[j])*60)
    return newminutes
    

def print_tasks(tasks,a):
    months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
              'Nov','Dec']
    b = newtime(a)
    for i in range(0, len(b)):
        print 'These are your tasks for ' + str(months[a[0]]) + str(a[1])
        print ''
        print 'Task Name: ' + task(a)[i]
        print ''
        print '     Start time: ', starttime(a)[i], ':', int(minutes(a)[i])
        print '     End time: ', newtime2(a)[i], ':', int(newminutes(a)[i])
        print '     Description: ' + description(a)[i]
        print ''

print print_tasks(tasks, [10,1])

    
