#Sum of digits of a number using recursion


def sum_of_digits(x):                   # Function takes in an integer x as its arguement
        '''Function to return the sum of digits of number, x'''
        assert isinstance(x,int)
        y = str(x)                      # x is converted to string and assigned to y
        if x > 0:                       # Applies recursion to positive integers
                if len(y) == 1:
                        return int(y[0])        # Recursion base case (if length of the string y is equal to 1)
                else:
                        return int(y[-1]) + sum_of_digits(int(y[0:-1]))
        else:                           # Applies recursion to negative integers
                if len(y) == 2:
                        return int(y[1])
                else:
                        return int(y[-1]) + sum_of_digits(int(y[1:-1]))
                
          
                
        
        
