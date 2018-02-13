# Problem Set 6
# Name: Kim,Matthew
# Collaborators: Lim, Jeremy

import sys # sys.maxint gives you the largest int that you can have in Python.

def read_file():
    """Read the imdb.txt file and return a list of [movie, actor, movie,
    actor, movie, etc.] """
    # Please do not change anything in this function. Just call it in your
    # other functions to get the master_list.
    file_object = open('imdb.txt', 'r')
    master_list = [line.strip() for line in file_object]
    file_object.close()
    return master_list

def make_title_dict():
    """Create the title-actors dictionary for Part 1.
    The keys are movie titles. The value associated with each key (movie) is
    the set representing the cast of that movie.
    """
    # getting the master_list
    master_list = read_file()
    title_actor = {}
    for j in range(0, len(master_list), 2):
        title = master_list[j]
        actor = master_list[j+1]
        if title not in title_actor:
            title_actor[title] = {actor}
        else:
            title_actor[title].add(actor)
    return title_actor

def make_actor_dict():
    """This function creates the actor-titles dictionary for Part 2.
    The keys are actors. The value associated with each key (actor) is the
    set of movies that the actor has been in.
    """
    # rest of your function goes here.
    master_list = read_file()
    actor_title = {}
    for j in range(0, len(master_list), 2):
        title = master_list[j]
        actor = master_list[j+1]
        if actor not in actor_title:
            actor_title[actor] = {title}
        else:
            actor_title[actor].add(title)
    return actor_title

def make_colloboration_dict(actor_title, title_actor):
    """This function creates the collaboration dictionary for Part 3.
    The keys are actors. The value associated with each key (actor) is the
    set of actors who have worked with the key actor in at least a film.
    """
    # rest of your function goes here.
    actor_collaborators = {}
    for A,V in actor_title.items():
        acollab = set()
        for M in actor_title[A]:
            acollab.update(title_actor[M])
        acollab.remove(A)
        actor_collaborators[A] = acollab
    return actor_collaborators
            


    

###########################################
def part1(title_actor):
    """Part 1--Use the movie title -> actors dictionary."""
    print '(Part 1) Using the title-actor dictionary to answer questions.'
    print '\t(A) How many actors are in the largest cast?'
    b = []
    z = []
    zb = set()
    c = set()
    for key,value in title_actor.items():
        a = len(value)
        b.append(a)
    print max(b)
    print '\t(B) What film (films) has (have) the largest cast?'
    for key, value in title_actor.items():
        if len(value) == 378:
            print key
    print '\t(C) How many films are there in the database?'
    for key, value in title_actor.items():
        z.append(key)
    lmao = set(z)
    print len(lmao)    
    print '\t(D) What is the size of the smallest cast?'
    for key,value in title_actor.items():
        a = len(value)
        b.append(a)
    print min(b)
    print '\t(E) What film (films) has (have) the smallest cast?'
    for key, value in title_actor.items():
        if len(value) == 1:
            print key
    print '\t(F) What is the average size of the cast in the database?'
    for keys, values in title_actor.items():
       for n in values:
           zb.add(n)
    print len(zb)/len(lmao)
    print '\t(G) Did Tom Hanks appear in Catch Me If You Can?'
    if 'Tom Hanks' in title_actor.get('Catch Me If You Can'):
        print 'Yes'
    else:
        print 'False'
    print '\t(H) List all the movies in which Owen Wilson has appeared:'
    lol = []
    for key in title_actor.keys():
        if 'Owen Wilson' in title_actor[key]:
            lol.append(key)
            lolsort = sorted(lol)
    for n in range(0,len(lolsort)):
        print lolsort[n]
    
    print '\t(I) List all the actors who appeared in both Silver Linings Playbook and American Hustle:'
    SLP = title_actor['Silver Linings Playbook']
    AH = title_actor['American Hustle']
    SLPAH = list(sorted(SLP.intersection(AH)))
    for n in range(0, len(SLPAH)):
        print SLPAH[n]
    # the rest of your function goes here.
    return None

def part2(actor_title):
    """Part 2--Use the actor -> movie titles dictionary."""
    print '*' * 10
    print '(Part 2) Using the actor-title dictionary to answer questions.'
    print '\t(A) [Again] List all the movies in which Owen Wilson has appeared.'
    owen = sorted(actor_title['Owen Wilson'])
    for n in range(0,len(owen)):
        print owen[n]
    print '\t(B) How many actors are there in the database?'
    numactor = []
    for keys, values in actor_title.items():
        numactor.append(keys)
    print len(numactor)
    print '\t(C) Which actor (actors) has (have) been in the'
    print 'largest number of films in the database?'
    leftshoe = []
    for keys, values in actor_title.items():
        rightshoe = len(values)
        leftshoe.append(rightshoe)
    myleftshoe = max(leftshoe)
    for keys, values in actor_title.items():
        if len(actor_title[keys]) == myleftshoe:
            print keys
    print '\t(D) Did Tom Hanks appear in Catch Me if You can?'
    if 'Catch Me If You Can' in actor_title['Tom Hanks']:
        print 'yes'
    final = []
    print '\t(E) What are all the films that both Jennifer Lawrence and Bradley Cooper have been in?'
    JL = actor_title['Jennifer Lawrence']
    BC = actor_title['Bradley Cooper']
    JLBC = list(sorted(JL.intersection(BC)))
    for n in range(0,len(JLBC)):
        print JLBC[n]
        
    # the rest of your function goes here.
    return None

def part3(actor_collaborators):
    """Part 3--Use the collaboration graph."""
    print '*' * 10
    print '(Part 3) Using the actor-collaborators dictionary to answer questions.'
    print '\t(A) Who is the actor with the most collaborators?'
    # the rest of your function goes here.
    hisrightshoe = []
    for keys, values in actor_collaborators.items():
        hisrightshoe.append(len(values))
    hisleftshoe = max(hisrightshoe)
    for keys, values in actor_collaborators.items():
        if len(actor_collaborators[keys]) == hisleftshoe:
            print keys, 'has the highest number of collaborators: ', hisleftshoe
    print '\t(B) Is Kate Winslet a collaborator of Cate Blanchett?'
    if 'Kate Winslet' in actor_collaborators.get('Cate Blanchett'):
        print 'yes'
    else:
        print 'no'
    print '\t(C) Is Kate Winslet a collaborator of a collaborator of Cate Blanchett?'
    rightflipflop = actor_collaborators['Kate Winslet']
    leftflipflop = actor_collaborators['Cate Blanchett']
    rightleft = rightflipflop.intersection(leftflipflop)
    if len(rightleft) >= 1:
        print 'yes'
    else:
        print 'no'
            
    print '\t(DPrint the actors who have collaborated with both Kate Winslet and Cate Blanchett.'
    rightflipflop = actor_collaborators['Kate Winslet']
    leftflipflop = actor_collaborators['Cate Blanchett']
    lololol = []
    for lolol in rightflipflop:
        if lolol in leftflipflop:
             lololol.append(lolol)
             ololo = sorted(lololol)
    for olo in ololo:
        print 'Kate Winslet ', '-> ', olo,' ->', ' Cate Blanchett'
    return None


def assignment():
    """Solve the different parts of pset 6."""
    
    ## ******** PART 1 *********
    ## Uncomment the following two lines when your part1 function is ready.
    title_actor = make_title_dict()
    part1(title_actor) # function call to print answers to Part 1

    ## ******** PART 2 *********
    ## Uncomment the following two lines when your part2 function is ready.
    actor_title = make_actor_dict()
    part2(actor_title) # function call to print answers to Part 2

    ## ******** PART 3 *********
    ## Uncomment the following two lines when your part3 function is ready.
    actor_collaborators = make_colloboration_dict(actor_title, title_actor)
    part3(actor_collaborators) # function call to print answers to Part 3
    return None

# Please leave this function call here so when we run the script, it would
# print output for us.
assignment()
