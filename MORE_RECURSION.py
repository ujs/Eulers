##1. Write a recursive function to return 1^2 + 2^2 + 3^2+ .....n^2 if you are given n.

def sum_of_squares(n):
    assert n>0 and isinstance(n,int), "Please enter positive integer"
    if n == 1:
        return 1
    else:
        return n**2 + sum_of_squares(n-1)



##2.Write a recursive Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)


def add_series(n,x):
    while n-x>=0:
        if n == x:
            return n
        else:
            return n + add_series(n-x,x)


##3. Write a recursive Python program to calculate the harmonic sum of n.
##Note : The harmonic sum is the sum of reciprocals of the positive integers. 

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)


##4. Write a recursive progrAM to calculate the value of 'a' to the power 'b'.

def a_power_b(a,b):
    if b == 0: return 1
    elif b ==1: return a
    else:
        return a * a_power_b(a,b-1)


##5. Write a recursive Python program to calculate the harmonic sum of n such that the output is as follows:
##      1/2 + 1/2^2 + 1/2^3 +.....+ 1/2^n
 

def harmonic_sum_2(n):
    if n == 0:
        return 0
    else:
        return 1/2**n + harmonic_sum_2(n-1)
