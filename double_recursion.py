def f(s):
    '''double recursion'''
    if len(s) <= 1:
        return s
    else:
        return f(f(s[1:])) + s[0] #Note double recursion
        

print (f('mat'))



