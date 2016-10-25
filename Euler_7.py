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

counter = 1
test_number = 3
while counter != 10001:
    if prime(test_number) == True:
        counter += 1
    
    test_number = test_number + 2

print (test_number-2)
    
        
    
