#Function returns the number of digits in the given number without decimals.

def countdigits(num):
        i = 1    # digit counter
        q = 1  	 # quotient captured after dividing by 10
        while q >= 1:  # the loop runs till quotient becomes a decimal
                q = abs(num)/10
                num = int(q)
                if q<1:		# skips line 11 as soon as q becomes <1
                        break
                i = i + 1

        print (i)


