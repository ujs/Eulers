## The sum of the squares of the first ten natural numbers is,

## 1^2 + 2^2 + ... + 10^2 = 385
## The square of the sum of the first ten natural numbers is,

## (1 + 2 + ... + 10)^2 = 552 = 3025

## Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
## Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    assert n>0 and isinstance(n,int), "Please enter positive integer"
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)


# Sum of all positive integers upto a given number
def add_integers_upto(num):
    '''Returns the sum of all positive integers upto num'''
    if num == 0: return 0
    elif num == 1: return 1
    else:
        return num + add_integers_upto(num-1)


def euler_6(n):
    return (add_integers_upto(n)**2) - sum_of_squares(n)
