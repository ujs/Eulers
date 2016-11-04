# Question 1 MIT OCW PS 3
#Without Recursion

from string import *
def countSubStringMatch(target,key):
    '''Returns the number of times the key string occurs in the target string'''
    counter = 0
    index = str.find(target,key)
    while index != -1:
        index = str.find(target,key,index+1)
        counter += 1
    return counter


#With Recursion

def countSubStringMatchRecursion(target,key):
    '''Uses recursion & returns the number of times the key string occurs in the target string'''
    index = str.find(target,key)
    if index == -1: return 0
    else:
        return 1 + countSubStringMatchRecursion(target[index+1:],key)

def test_countSubStringMatchRecursion():
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","atgc"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","at"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","cat"))
    print(countSubStringMatchRecursion("atgacatgcacaagtatgcat","agyj"))


# Question 2 MIT OCW PS 3
def subStringMatchExact(target,key):

    tuple = ()
    index = str.find(target,key)
    while index != -1:
        tuple += (index, )
        index = str.find(target,key,index+1)
    return tuple

    
    
