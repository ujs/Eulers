#Print out a pascal triangle

def pascal(n):
    if n == 1:
        return [1]
        
    else:
        previous_line = pascal(n-1)
        triangle = [1]
        for i in range (0, len(previous_line)-1):
            triangle.append(previous_line[i] + previous_line[i+1])
        triangle += [1]
        
    return triangle
        
            
print(pascal(2))     


    
