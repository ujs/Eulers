x = 11111
sum = 0
i = 10000
q = x//i
r = x % i
while i >1:
	
	sum = sum + q
	i = i/10
	q = r//i
	r = r % i
	

print (sum + q)
