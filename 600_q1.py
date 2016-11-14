## Ques 4
def findAll(wordList, letters):
    """assumes: wordList is a list of words in lowercase. lStr is a str of lowercase letters.
     No letter occurs in lStr more than once
     returns: a list of all the words in wordList that contain
     each of the letters in lStr exactly once and no
     letters not in lStr."""
    result = []
    letters = sorted(letters)
    for i in wordList:
        w = sorted(i)
        if w == letters:
            result.append(i)
    return result
