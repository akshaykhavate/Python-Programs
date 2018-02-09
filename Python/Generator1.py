def fs(n):
    i=1
    while i<=n:
        res=fib(i)
        i+=1
        yield res
    raise stopIteration

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    return fib(n-1)+fib(n-2)
