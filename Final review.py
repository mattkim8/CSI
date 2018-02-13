##
##adding stuff to dictionaries
##d = {}
##d['computer science'] = 10
##str_list = ['a', 'b', 'c', 'string', 'anotherkey', 'something']
##num_list = [1,10,-1,1000,10,5]
##
##d = {}
##for i in range(len(str_list)):
##    d[str_list[i]] = num_list[i]
##
##print d


##filename = 'practice.txt'
##f = open(filename, 'r')
### f can be though of as a list of strings. What is each string in that list?
### each line in the file
##
##
##filename = 'practice2.txt'
##f = open(filename, 'w')
##for i in range(10):
##    f.

import os

def walk(dir_name):
    for name in os.listdir(dir_name):
        path = os.path.join(dir_name, name)
        if os.path.isfile(path):
            print name
        else:
            walk(path)
    return None

cwd = os.getcwd()
walk(cwd)
