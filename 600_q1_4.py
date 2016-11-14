def findAll(wordList, letters):
    result = []
    letters = sorted(letters)
    for w in wordList:
        w = sorted(w)
        if w == letters:
            result.append(w)
    return result
