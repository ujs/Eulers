even = 0
odd= 0
numbers = (1,3,7,89,6)
for i in range(0,len(numbers)):
    if numbers[i]%2 == 0:
        even +=1
    else:
        odd +=1

print ('number of even numbers:' + str(even))
print ('number of odd numbers:' + str(odd))
