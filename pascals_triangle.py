#Print out a pascal triangle

def pascal(n):
    if n == 1:
        return [1]
        
    else:
        previous_line = pascal(n-1)
        last_line = [1]
        for i in range (0, len(previous_line)-1):
            last_line.append(previous_line[i] + previous_line[i+1])
        last_line += [1]
        return last_line
        
                
for i in range (1,6):
        print (pascal(i))


    
