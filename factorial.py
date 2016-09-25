#Calculate factorial of given number x.
x = 6
ans = 1 # variable to store ans after multiplication
i = 2	# intialize loop variable
while i <= x:
	ans = i * ans
	i = i +1

print (ans)  # print final ans. i.e factorial
