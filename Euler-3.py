
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143


import time
start_time = time.time()


num = 600851475
factors = [] #list to store all factors

def prime(x):                       #Function to test if Number prime or not
    j = 0                           #divisor counter
    

    for i in range(2,x):
        if x%i == 0:
            j = j+1
            return False
            break
    if j == 0:
        return True
        


for f in range(2, num+1):
    if num%f == 0 and prime(f) == True:
        factors += [f]

l = max(factors)
print ('all factors are: ' + str(factors))
print ('largest prime factor is: ' + str(l))

print("--- %s seconds ---" % (time.time() - start_time))    #Calculates execution time of the program
