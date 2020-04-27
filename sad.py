import random

def combination(options):
        #Initial variables
    x = 1
    
    sets=["a","b"]
    group = []
    if options==12:
        while x < 13:
            random.shuffle(sets)
            group.append("%s%s" % (x, sets[0]))
            x+=1
        return group
    elif options==10:
        while x < 11:
            random.shuffle(sets)
            group.append("%s%s" % (x, sets[0]))
            x+=1
        return group
    else:
        return "There has been an error"