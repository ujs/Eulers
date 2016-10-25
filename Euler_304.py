def prime(x):                       #Function to test if Number prime or not
        '''Checks whether x is prime or not'''
        if x <= 0 or isinstance(x, float):
            return None
            print ("x should be a positive integer. Please try again")
        else:
            for i in range(2,x):
                if x%i == 0:
                    return False
                    break
            return True

def next_prime(n):
    '''For any positive integer n the function next_prime(n) returns the smallest prime p such that p>n.'''
    n +=1
    while not prime(n):
        n += 1
    return n

def a(n):
    if n == 1:
        return next_prime(10**14)
    else:
        return next_prime(a(n-1))

def f(n):
    '''Returns the nth fibonacci number'''
    if n < 0 or isinstance(n, float):
        return print ("Please enter a positive integer")
    else:
        if n == 0: return 0
        elif n == 1: return 1
        else: return f(n-1) + f(n-2)

def b(n):
    return f(a(n))

def euler_304():
    summation = 0
    for i in range (1,100001):
        summation += b(i)
    return summation
        
