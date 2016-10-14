# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

j = 0

for x in range(10,2600,10):
    for i in range (1,11):
        if x % i == 0:
            j +=1
    
    if j == 10:
        print(x)
        break
    j = 0  
    
   
    
  
    

    
