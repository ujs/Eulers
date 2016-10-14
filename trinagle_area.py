def area(b,h):
    '''Calculates area of triangle'''
    if h >=0 and b >=0:
        a = 0.5*b*h
        return a

    else:
        print ("enter positive lengths")
        return None



def db(b,h):
    '''Calculates double of triangle area'''
    if h >=0 and b >=0:
        b=area(b,h)*2
        return b

    else:
        print ("double only positive lengths")
        return None
    


def sq(b,c):
    '''Calculates area of square'''
    a=b*c
    return a

def sa(a,b):
    '''Calculates surface area of a cube'''
    s=6*sq(a,b)
    return s
