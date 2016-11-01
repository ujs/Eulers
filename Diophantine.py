

largest_impossible = []

for n in range (900,1000):
    for a in range (n/6):
        for b in range (n/6):
            for c in range (n/6):
                combination_nuggets = 6*a + 9*b + 20*c
                if n == combination_nuggets:
                    print (n, "is a combination of ", a, b, c, " times ", "6", "9", "20")
                    if n!=combination_nuggets: largest_impossible.append(n)

print max(largest_impossible)
                    
