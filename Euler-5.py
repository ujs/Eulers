# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? Ans 232792560

def divisibility_check(num,n1,n2):
    '''Returns whether num is divisible by all positive integers from n1 to n2'''

    counter = 0
    for i in range(n1,n2+1):    #Checks if num is divisible by all numbers from n1 to n2
        if num%i == 0:          
            counter += 1
        else: break             #As soon as the loop finds that num is not divisible, it breaks and returns False
    if counter == n2+1-n1:
        return True
    else:
        return False
        



def euler_5(n1,n2):
    '''Returns the smallest positive number that is evenly divisible by all of the numbers from n1 to n2'''
    import time
    start_time = time.time()
    a = n2
    while divisibility_check(a,n1,n2) == False:
        a = a + n2
    print ("Program Execution Time (in seconds) is : " + str(time.time()-start_time))
    return a
