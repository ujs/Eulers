# Calculate all the divisors of positive integer x



def divisors(x):
       import time
       start_time = time.time()
       '''Returns all the divisors of x which are <= itself '''
       if x >= 1 and isinstance (x, int):
              for i in range (1,x+1):  # loop checks from 1 to x. Calculates remainder to check divisibility
                     if x%i == 0 :
                            print (i)  # prints each divisor in separate line
                     i = i + 1	
       else:
                                  
              print ('Invalid input- x should be a positive integer greater than 1')
              return None

       
       print("--- %s seconds ---" % (time.time() - start_time))
