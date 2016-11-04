def bsearch(num, e, first, last):
    if (last-first) < 2: return num[0] == e or num[-1] == e
    else:
        mid = int((first + last)/2)
        #if num[mid] == e: return True
        if mid > e: return bsearch(num, e, first, mid-1)
        else: return bsearch(num, e, mid + 1, last)

def test_bsearch():
    
    print(bsearch([1,4,5,7,11,23,32],11,1,32))
    print (bsearch([1,4,5,7,11,23,32],100,1,32))
    
