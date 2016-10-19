
# To check if given number or word is a palindrome

def is_palindrome(c):
    '''Returns whether the given input is a palindrome or not'''
    c= str(c)
    if len(c) == 0 or len(c) == 1:
        return True
    else:
        if c[0] == c[-1] and is_palindrome(c[1:-1]):
            return True
        else:
            return False



# Fibonacci
def fibonacci(n):
    '''Returns the nth fibonacci number'''
    if n < 0 or isinstance(n, float):
        return print ("Please enter a positive integer")
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)


# Factorial of a number
def factorial(n):
    '''Returns the factorial of n'''
    if n < 0 or isinstance(n, float):
        return print ("Please enter a positive integer")
    else:
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n-1)


# Sum of numbers in list
c = [3,5,6,2]
def add_list(c):
    '''Returns the sum of numbers in list'''
    if len(c) == 1:
        return c[0]
    elif len(c) == 0:
        print ("The list is empty")
        return None
    else:
        return c[0] + add_list(c[1:])



# Maximum of a list
c = [300,5,6,20000,2334534,424545763,23432536,23,52,45,2]
def maximum_list(c):
    '''Returns the maximum value in the given list'''
    if len(c) == 1:
        return c[0]
    elif len(c) == 0:
        print ("The list is empty")
        return None
    else:
        if c[0] > maximum_list(c[1:]):
            return c[0]
        else:
            return maximum_list(c[1:])




# Sum of all positive integers upto a given number
def add_integers_upto(num):
    '''Returns the sum of all positive integers upto num'''
    if num == 0: return 0
    elif num == 1: return 1
    else:
        return num + add_integers_upto(num-1)
