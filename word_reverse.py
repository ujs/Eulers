j = -1
x = input('enter a word: ')
y = []
for i in range (0, len(x)):
    y += x[j]
    j = j-1

print (str(y))
