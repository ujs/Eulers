def is_palindrome():
    '''Checks if the word entered as input is a palindrome or not'''
    j = -1
    x = input('enter a word: ')
    y = ''
    for i in range (0, len(x)):
        y += x[j]
        j = j-1

    if y == x:
        print ('This word is a palindrome')
        return True
    else:
        print ('This word is not a palindrome')
        return False
