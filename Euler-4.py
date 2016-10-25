
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import time
start_time = time.time()

def is_palindrome(c):
    '''Function uses recursion to find out if input is a palindrome or not'''
    s = str(c)
    if len(s)<=1:
        return True
    else:
        if s[0] == s[-1] and is_palindrome(s[1:-1]):
            return True
    return False

list = []  #initiating empty list chich will collect palindromes
for i in range(100,1000):       #
    for j in range(i,1000):
        c = i*j
        e = str(c)

        if is_palindrome(e):
            list += [c]

print (max(list))

print("--- %s seconds ---" % (time.time() - start_time)) 



