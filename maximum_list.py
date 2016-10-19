
def f(c):
    if len(c) == 1:
        return c[0]
    else:
        if c[0] > f(c[1:]):
            return c[0]
        else:
            return f(c[1: ])
        
