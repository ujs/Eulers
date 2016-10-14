
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time = time.time()

list = []  #initiating empty list chich will collect palindromes
for i in range(100,1000):       #
    for j in range(100,1000):
        c = i*j
        e = str(c)
        d = ''
        for k in range(len(str(c))-1,-1,-1):
            d = d + e[k]
        
        if d == e:
            list += [c]

print (max(list))

print("--- %s seconds ---" % (time.time() - start_time)) 
