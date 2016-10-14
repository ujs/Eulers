# Compute square root of given number

def sq_root(x):
        '''Calculates the square root of x'''
        i = 1

        if x == 0:
                return 0
        if x < 0:
                print("can't find squareroot of negative number")
                return None

        else:
            while i * i < x:
                i = i + 1
            if i * i == x:
                return i
            else:
                print('not perfect square')
                return None

    



    

    

    
