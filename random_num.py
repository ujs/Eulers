#Generate random number. Ask for user to guess until she selects the right number

import random

r = random.randrange(1,10)

x = 0

while x !=r:
    
    x = int(input ("enter a random number from 1 to 9: "))

print ('Good guess, You selected the right number ' + str(x))



