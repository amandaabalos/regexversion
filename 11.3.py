#import regex library
import re

newlist=list()
finallist=list()

hand=open('regex_sum_300344.txt')
#fh=hand.read()
#print(fh)

for line in hand:
#strip the space at the right end of each line
    #line=line.rstrip()
    #print(line)


    stuff=re.findall('[0-9]+', line)
    if len(stuff) == 0: continue
    #print(stuff)

    for ind in stuff:
        wd=ind.split()
        #print(wd)

        for wds in wd:
            num = int(wds)
            #print(num)


#append into list called newlist

            newlist.append(num)
print(sum(newlist))






    #for index in stuff, convert string to integer
    #for word in stuff:
    #    wd = word.split()
    #print(wd)


        #num = int(word)
    #print(num)
        #append into list called newlist
    #    newlist.append(num)
#print(sum(newlist))








    #newlist.append(stuff)
#print(newlist)

    #num = float(stuff[0])
    #newlist.append(num)
#print(sum(newlist))





#intlist=[int(x) for x in input().split()]
#print(intlist)
#newlist=[int(i) for i in newlist]


#print(newlist)
#for i in newlist:
#    split=i.split()
#print(split)

    #for ints in stuff:
    #    ints=stuff.split()
    #    print(ints)

    #if None in stuff:
    #    continue
    #else:
    #    newlist.append(stuff)
    #print(newlist)
