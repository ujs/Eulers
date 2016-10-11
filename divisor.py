# Calculate all the divisors of positive integer x

import time
start_time = time.time()

x = 90  
for i in range (1,x+1):  # loop checks from 1 to x. Calculates remainder to check divisibility
       if x%i == 0 :
              print (i)  # prints each divisor in separate line
       i = i + 1	

if x<1:                  # if x < 1, then divisors are not computed. Instead print message   
       print ('Invalid input- x should be a positive integer greater than 1')



print("--- %s seconds ---" % (time.time() - start_time))
