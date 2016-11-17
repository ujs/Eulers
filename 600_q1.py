## Ques 4
def findAll(wordList, letters):
    """assumes: wordList is a list of words in lowercase. lStr is a str of lowercase letters.
     No letter occurs in lStr more than once
     returns: a list of all the words in wordList that contain
     each of the letters in lStr exactly once and no
     letters not in lStr."""
    ans = []
    letters = sorted(letters)
    for i in wordList:
        w = sorted(i)
        if w == letters:
            ans.append(i)
    return ans


## Ques 5
v1 = [1,-2,-4]
v2 = [0,3,-1,3]
def addVectors(v1, v2):
     """assumes v1 and v2 are lists of ints.
     Returns a list containing the pointwise sum of
     the elements in v1 and v2. For example,
     addVectors([4,5], [1,2,3]) returns [5,7,3],and
     addVectors([], []) returns []. Does not modify inputs."""
     if len(v1) > len(v2):
         result = v1[:]
         other = v2[:]
     else:
         result = v2[:]
         other = v1[:]
     
     for i in range(len(other)):
         result[i] += other[i]
     print ('the sum of two vectors', v1, 'and', v2, 'is', result)    
     return result

## Ques 6
def f(s, d):
    for k in d.keys():
        d[k] = 0
    for c in s:
        if c in d:
            d[c] += 1
        else: d[c] = 0
    return d
def addUp(d):
     result = 0
     for k in d:
         result += d[k]
     return result
d1 = {}
d2 = d1
d1 = f('abbc', d1)
print addUp(d1)
d2 = f('bbcaa', d2)
print addUp(d2)
print f('', {})
print result 
     
