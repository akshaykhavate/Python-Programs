import os
def fs(n):
    i=0
    while i<=n:
        res=fact(i)
        i+=1
        yield res
    raise stopIteration

def fact(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
        return fac
    raise stopIteration
