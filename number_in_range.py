# Function to check if a positive integer is in the given range

def number_in_range(n, a, b):
    '''Checks if n lies between a and b. n has to be a positive integer.'''
    if n<=0 or isinstance(n, float):
            return print("Please enter positive integer values")
    else:
        for i in range (a, b):
            if n == i:
                return print ("Yes this number is in the given range")
                break
        return ("Not in given range")
