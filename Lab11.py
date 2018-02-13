#Lab 5

def read_file(x):
    restaurants = dict()
    try:
        file_handle = open('restaurant.txt','r')
        for line in file_handle:
                stripped_line = line.rstrip()
                split_line = stripped_line.split(',')
                restaurants[split_line[2]] = (split_line[0],split_line[1],split_line[3],split_line[4])
                if 
    except IOError:
        print "file doesn't exist"
    except ValueError:
        print line
        print 'there are not 5 values'
            
                        
        
