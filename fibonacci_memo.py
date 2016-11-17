

##Calculating nth fibonacci number without memoisation
    
def fib(n):
    if n <= 1:
        return 1
    else: return fib(n-1) + fib(n-2)

    

##Calculating nth fibonacci number with memoisation

def fib1(n):
    memo = {0:0, 1:1}
    return fastFib(n, memo)

def fastFib(n, memo):
    print ('fib1 called with', n)
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]





