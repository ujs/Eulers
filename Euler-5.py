# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisibility_check(num,n):
    '''Returns whether num is divisible by all positive integers upto n'''

    counter = 0
    for i in range(2,n+1):
        if num%i == 0:
            counter += 1
        else: continue
    if counter == n-1:
        return True
    else:
        return False
        



def euler_5(a,n):
    '''Returns the smallest positive number that is evenly divisible by all of the numbers upto n'''
    starting_point = n
    while divisibility_check(a,n) == False:
        a = a + starting_point
    return a









    
   
    
  
    

    
