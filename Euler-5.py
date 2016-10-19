# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def euler_5(y,z):
    '''Calculates the smallest number that is divisible by all numbers from y to z'''
    
    j = 0

    for x in range(400000,999999999,20):
        for i in range (y,z+1):
            if x % i == 0:
                j +=1
        
        if j == (z+1)-y:
            return x
            break
        else:
            j = 0
    


    
   
    
  
    

    
