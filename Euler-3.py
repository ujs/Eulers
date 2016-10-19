
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143


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

def euler_2(num):
    '''Returns the largest prime factor of num'''
    import time
    start_time = time.time()
        
    for f in range(int((num+1)/2),2,-1):           #Checking if the factors of num are prime or not and adding to a list
        if num%f == 0 and prime(f) == True:
            print ('largest prime factor is: ' + str(f))
            break

    print("--- %s seconds ---" % (time.time() - start_time))    #Calculates execution time of the program



##def euler_2(num):
##    '''Returns the largest prime factor of num'''
##    import time
##    start_time = time.time()
##    factors = []                        #list to store all factors
##    for f in range(2,(num+1)/2):           #Checking if the factors of num are prime or not and adding to a list
##        if num%f == 0 and prime(f) == True:
##            factors += [f]
##
##    l = max(factors)                    #Finds the largest prime factor in the list
##    print ('all factors are: ' + str(factors))
##    print ('largest prime factor is: ' + str(l))
##
##    print("--- %s seconds ---" % (time.time() - start_time))    #Calculates execution time of the program
##
